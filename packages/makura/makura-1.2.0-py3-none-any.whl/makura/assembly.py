#!/usr/bin/env python3
import argparse
import sqlite3
import concurrent.futures
import hashlib
import itertools
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from time import sleep

import pandas as pd
import requests
from tqdm import tqdm

import makura
from makura import PKG_PATH, DATA_DIR, __version__
from makura.taxonparse import TaxonomyParser
from makura.api import app

AGLEA_TAXIDS = [
    2836,
    304574,
    29197,
    131213,
    3041,
    2825,
    304573,
    3027,
    39119,
    2864,
    3035,
    5747,
    38254,
    2830,
    131220,
    96475,
    2870,
    82162,
    569578,
    38410,
    2763,
    2833,
]


class AssemblySummary:
    _REFSEQ_GROUPS = [
        "archaea",
        "bacteria",
        "fungi",
        "invertebrate",
        "plant",
        "protozoa",
        "vertebrate_mammalian",
        "vertebrate_other",
        "viral",
    ]

    _GENBANK_GROUPS = [
        "archaea",
        "bacteria",
        "fungi",
        "invertebrate",
        "metagenomes",
        "other",
        "plant",
        "protozoa",
        "unknown",
        "vertebrate_mammalian",
        "vertebrate_other",
        "viral",
    ]

    _REFSEQ_CATEGORY = ["na", "reference genome", "representative genome"]

    _ASSEMBLY_LEVEL = ["Chromosome", "Complete Genome", "Contig", "Scaffold"]

    microbial_grops = [
        "archaea",
        "bacteria",
        "fungi",
        "viral",
        "protozoa",
        "invertebrate",
        "aglea",
    ]

    def __init__(self):
        self.assembly_summary_dir = DATA_DIR
        self.assembly_summary_dir.mkdir(exist_ok=True)
        self.assembly_summary_db = self.assembly_summary_dir / "assembly_summary.db"

        self.updated = False
        if not self.assembly_summary_db.is_file():
            if not self.assembly_summary_db.is_file():
                self.update_assembly_summary()
                self.updated = True

    def connect_db(self):
        self.db_conn = sqlite3.connect(self.assembly_summary_db)

    def close_db(self):
        self.db_conn.close()

    def use_sql(func):
        def wrap(*args, **kwargs):
            self = args[0]
            self.connect_db()
            result = func(self, *args[1:], **kwargs)
            self.close_db()
            return result

        return wrap

    @use_sql
    def get_assembly_summary_cols(self):
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT * FROM assembly_summary")
        return [i[0] for i in cursor.description]

    @use_sql
    def update_assembly_summary(self):
        if self.assembly_summary_db.is_file():
            self.assembly_summary_db.unlink()

        taxparser = TaxonomyParser()
        taxparser.update_taxonomy_database()
        for groups, db_type in zip(
            (self._REFSEQ_GROUPS, self._GENBANK_GROUPS), ("RefSeq", "GenBank")
        ):
            print(f"update {db_type} database")
            rows = []
            for group in groups:
                url = f"https://ftp.ncbi.nlm.nih.gov/genomes/{db_type.lower()}/{group}/assembly_summary.txt"
                response = requests.get(url)
                for row in response.text.split("\n"):
                    if row.startswith("#   See ") or not row:
                        continue
                    elif row.startswith("#"):
                        cols = row.strip("# ").strip().split("\t")
                    else:
                        row = f"{row}\t{group}".split("\t")
                        rows.append(row)
                print(f"Get the {group} of assembly summary", file=sys.stderr)

            cols.append("group")
            assembly_summary_df = pd.DataFrame(rows, columns=cols)

            taxids = [
                str(taxid) for taxid in assembly_summary_df["taxid"].to_list() if taxid
            ]

            taxid2lineage_dct = dict(
                [(taxid, taxparser.get_lineage(taxid)) for taxid in taxids]
            )

            all_rank_taxids = all_rank_taxids = list(
                set(
                    list(itertools.chain.from_iterable(taxid2lineage_dct.values()))
                ).union(set(taxids))
            )
            taxid2name_dct = taxparser.get_taxid_translator(all_rank_taxids)
            taxid2rank_dct = taxparser.get_rank(all_rank_taxids)
            taxid_rows = []
            for taxid in taxids:
                lineage = taxid2lineage_dct[taxid]
                row = ";".join(
                    [
                        "|".join([str(t), taxid2rank_dct[t], taxid2name_dct[t]])
                        for t in lineage
                    ]
                )
                taxid_rows.append(row)
            taxid_df = pd.DataFrame(taxid_rows, columns=["taxid_lineage"])

            assembly_summary_df = pd.concat([assembly_summary_df, taxid_df], axis=1)
            assembly_summary_df = assembly_summary_df.set_index("assembly_accession")
            self.connect_db()
            assembly_summary_df.to_sql(
                "assembly_summary",
                self.db_conn,
                if_exists="append",
                index=True,
                index_label="assembly_accession",
            )
            self.db_conn.commit()

    @use_sql
    def filter_accession_by_group(self, groups=[]):
        cursor = self.db_conn.cursor()
        cursor.execute(
            f"SELECT assembly_accession FROM assembly_summary WHERE `group` IN ({','.join(['?']*len(groups))})",
            groups,
        )
        accessions = [res[0] for res in cursor.fetchall()]
        return accessions

    def download_by_group(self, out_dir, groups=[]):
        accessions = self.filter_accession_by_group(groups=groups)
        self.download_by_accession(out_dir, accessions)

    @use_sql
    def filter_accession_by_taxid(self, taxids=[]):
        cursor = self.db_conn.cursor()
        cursor.execute(
            f"SELECT assembly_accession,taxid_lineage,taxid FROM assembly_summary;"
        )
        asm_acc_ls = []
        taxids = set([str(t) for t in taxids])
        for row in cursor.fetchall():
            asm_acc, taxid_lineage, taxid = row
            if taxid_lineage is None or taxid is None:
                continue

            if taxids & set(
                [value.split("|")[0] for value in taxid_lineage.split(";")]
            ):
                asm_acc_ls.append(asm_acc)
        return asm_acc_ls

    def download_by_taxid(self, out_dir, taxids=[]):
        accessions = self.filter_accession_by_taxid(taxids=taxids)
        self.download_by_accession(
            out_dir=out_dir, accessions=accessions, use_rsync=True, parallel=4
        )

    def _download_job(self, ftp_path, out_dir, use_rsync=True):
        prefix = ftp_path.split("/")[-1]
        local_genome_file = Path(out_dir) / f"{prefix}_genomic.fna.gz"
        genome_url = f"{ftp_path}/{prefix}_genomic.fna.gz"
        md5checksums_url = f"{ftp_path}/md5checksums.txt"

        if use_rsync:
            genome_url = re.sub(r"^https", "rsync", genome_url)
            returncode = os.system(
                f"rsync --copy-links --times --quiet {genome_url} {out_dir}"
            )
            if returncode:
                print(
                    f"CMD: rsync --copy-links --times --quiet {genome_url} {out_dir}",
                    file=sys.stderr,
                )
                data = None
            else:
                data = local_genome_file

            with tempfile.NamedTemporaryFile("w", delete=False) as fp:
                tmp_file = Path(fp.name)
            md5checksums_url = re.sub(r"^https", "rsync", md5checksums_url)
            returncode = os.system(
                f"rsync --copy-links --times --quiet {md5checksums_url} {tmp_file}"
            )
            if returncode:
                md5checksums_content = None
            else:
                md5checksums_content = tmp_file.read_text()
                tmp_file.unlink()

        else:
            with requests.Session() as session:
                data = b""
                r = session.get(genome_url, stream=True)
                with open(local_genome_file, "wb") as f:
                    for chunk in r.raw.stream(4096, decode_content=False):
                        if chunk:
                            f.write(chunk)
                            data += chunk

                r = session.get(md5checksums_url)
                md5checksums_content = r.text

        original_md5 = ""
        if md5checksums_content:
            for md5_row in md5checksums_content.split("\n"):
                if md5_row:
                    md5_value, file = md5_row.split("  ")
                    if file == f"./{prefix}_genomic.fna.gz":
                        original_md5 = md5_value
                        break

        return (data, original_md5)

    @use_sql
    def download_by_accession(
        self, out_dir, accessions=[], use_rsync=True, parallel=4, debug=False
    ):
        if isinstance(accessions, str):
            accessions = [accessions]
        out_dir = Path(out_dir)

        cursor = self.db_conn.cursor()
        cursor.execute(
            f"SELECT assembly_accession,organism_name,ftp_path FROM assembly_summary WHERE assembly_accession IN ({','.join(['?']*len(accessions))})",
            accessions,
        )
        args = [(row[1], row[-1]) for row in cursor.fetchall() if row[-1] != "na"]

        def download_iter():
            for organism_name, ftp_path in args:
                yield organism_name, ftp_path

        def _job(organism_name, ftp_path):
            """
            returncode: return download status
            1: the genome file is existed, and skill it
            2: download task is success, and append the md5 of the file to md5checksums.txt
            3: download task is failed and remove the incomplete file
            """
            prefix = ftp_path.split("/")[-1]
            local_genome_file = out_dir / f"{prefix}_genomic.fna.gz"
            if local_genome_file.is_file():
                returncode = 1
            else:
                data, md5_value = self._download_job(ftp_path, out_dir, use_rsync)
                success = self.validate_md5(data, md5_value)
                if success:
                    file = f"./{local_genome_file.name}"
                    with open(out_dir / "md5checksums.txt", "a") as md5_h:
                        md5_h.write(f"{md5_value}\t{file}\n")
                    returncode = 2
                else:
                    local_genome_file.unlink(missing_ok=True)
                    returncode = 3

            return returncode

        with tqdm(total=len(args), desc="Download NCBI genomes") as pbar:
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=parallel
            ) as executor:
                futures = {
                    executor.submit(
                        _job,
                        *args,
                    ): args
                    for args in download_iter()
                }

                results = {}
                count = 0
                for future in concurrent.futures.as_completed(futures):
                    org_name, ftp_path = futures[future]
                    pbar.set_description(f"{org_name} is downloaded")
                    returncode = future.result()
                    results[ftp_path] = returncode
                    pbar.update(1)

                    if returncode != 1:
                        count += 1
                    if count == 500:
                        pbar.set_description(f"sleep 30s...")
                        sleep(30)
                        count = 0
        if debug:
            download_status_f = out_dir / "download_status.txt"
            with open(download_status_f, "w") as f:
                for ftp_path, returncode in results.items():
                    if returncode == 1:
                        message = "existed"
                    elif returncode == 2:
                        message = "success"
                    elif returncode == 3:
                        message = "failed"
                    else:
                        message = "unknown"
                    f.write(f"{ftp_path}\t{message}\n")

        return results

    @use_sql
    def filter_refseq_category(self, accessions=[], categories=[]):
        if not categories:
            categories = self._REFSEQ_CATEGORY
        cursor = self.db_conn.cursor()
        conditions = (
            f"assembly_accession IN ({','.join(['?']*len(accessions))}) AND"
            if accessions
            else ""
        )
        conditions = (
            f"{conditions} refseq_category IN ({','.join(['?']*len(categories))});"
        )
        query = f"SELECT assembly_accession FROM assembly_summary WHERE {conditions}"

        cursor.execute(
            query,
            accessions + categories,
        )

        return [row[0] for row in cursor.fetchall()]

    @use_sql
    def filter_assembly_level(self, accessions=[], levels=[]):
        if not levels:
            levels = self._ASSEMBLY_LEVELS

        cursor = self.db_conn.cursor()
        conditions = (
            f"assembly_accession IN ({','.join(accessions)}) AND" if accessions else ""
        )
        conditions = f"{conditions} assembly_level IN ({','.join(['?']*len(levels))});"
        cursor.execute(
            f"""SELECT assembly_accession 
            FROM assembly_summary 
            WHERE {conditions}
            """,
            accessions + levels,
        )
        return [row[0] for row in cursor.fetchall()]

    def select_microbiome(self):
        accessions = self.filter_accession_by_group(groups=self.microbial_grops)
        return accessions

    @staticmethod
    def sum_md5(data):
        if isinstance(data, Path):
            with open(data, "rb") as file_to_check:
                content = file_to_check.read()
        else:
            content = data
        md5_returned = hashlib.md5(content).hexdigest()

        return md5_returned

    @classmethod
    def validate_md5(cls, data, md5_value):
        """
        input a file path or string
        """
        if data is None or md5_value is None:
            return False

        md5_returned = cls.sum_md5(data)
        if md5_returned == md5_value:
            return True
        else:
            return False

    @staticmethod
    def uniq_md5checksums(md5checksums):
        md5checksums = Path(md5checksums)
        tmp_checksums = md5checksums.parent / f"{md5checksums.name}.tmp"
        with open(tmp_checksums, "w") as f:
            f.write(
                "\n".join(set([i for i in md5checksums.read_text().split("\n") if i]))
                + "\n"
            )
        tmp_checksums.rename(md5checksums)

    def check_genomes(self, md5checksums):
        """
        find which genomes are not in md5checksum.txt, and remove them.
        """
        md5checksums = Path(md5checksums)
        self.uniq_md5checksums(md5checksums)
        checked_files = set()

        with open(md5checksums, "r") as handle:
            for row in handle.readlines():
                row = row.strip("\n")
                if not row:
                    continue
                md5_value, genome_file = row.split("\t")
                genome_file = md5checksums.parent / Path(genome_file).name
                checked_files.add(genome_file.name)
        existed_file = set(
            [
                file.name
                for file in md5checksums.parent.iterdir()
                if file.name.endswith(".fna.gz")
            ]
        )
        need_removed = existed_file - checked_files

        [(md5checksums.parent / file).unlink() for file in need_removed]
        return list(need_removed)

    @use_sql
    def gen_summary(
        self,
        out_fmt="tab",
        accessions=[],
        taxids=[],
        groups=[],
        assembly_level=[],
        refseq_category=[],
    ):
        accessions = list(
            set(self.filter_accession_by_group(groups))
            | set(self.filter_accession_by_taxid(taxids))
            | set(accessions)
        )
        cols = self.get_assembly_summary_cols()
        self.connect_db()
        cursor = self.db_conn.cursor()
        cursor.execute(
            f"SELECT * FROM assembly_summary WHERE assembly_accession IN ({','.join(['?']*len(accessions))})",
            accessions,
        )
        filter_df = pd.DataFrame(cursor.fetchall(), columns=cols)

        if assembly_level:
            filter_df = filter_df[filter_df["assembly_level"].isin(assembly_level)]
        if refseq_category:
            filter_df = filter_df[filter_df["refseq_category"].isin(refseq_category)]
        if filter_df.shape[0] == 0:
            sys.stderr.write(
                "check input the right assembly source (refseq or genbank)\n"
            )
        if out_fmt == "tab":
            yield "\t".join(filter_df.columns)
            for _, row in filter_df.iterrows():
                yield "\t".join([str(i) for i in row.to_list()])
        else:
            for _, row in filter_df.iterrows():
                yield json.dumps(row.to_dict())


def main():
    def get_argument():
        class ExplicitDefaultsHelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
            def _get_help_string(self, action):
                if action.default in (None, False):
                    return action.help
                return super()._get_help_string(action)

        asm_levels = ["chromosome", "complete", "contig", "scaffold"]
        refseq_categories = ["reference", "representative", "na"]
        groups = [
            "archaea",
            "bacteria",
            "fungi",
            "invertebrate",
            "metagenomes",
            "other",
            "plant",
            "protozoa",
            "unknown",
            "vertebrate_mammalian",
            "vertebrate_other",
            "viral",
        ]

        def check_file(path):
            if not path:
                raise TypeError("Please input path")
            else:
                path = Path(path)
                if not path.exists():
                    raise argparse.ArgumentTypeError("No such as a file or directory")
                else:
                    return path
            raise TypeError("Please input path")

        def parse_dir(path):
            if not path:
                raise TypeError("Please input path")

            path = Path(path)
            path.mkdir(exist_ok=True)
            return path

        def split_comma(str_list):
            if str_list:
                return [i.strip() for i in str_list.split(",")]

        def check_levels(str_lvls):
            lvl_ls = split_comma(str_lvls)
            if set(lvl_ls) - set(asm_levels):
                raise ImportError(f"assembly-level must be {','.join(asm_levels)}")
            else:
                lvl_map = dict(
                    zip(
                        ["chromosome", "complete", "contig", "scaffold"],
                        ["Chromosome", "Complete Genome", "Contig", "Scaffold"],
                    )
                )
                return [lvl_map[lvl] for lvl in lvl_ls]

        def check_refseq_category(str_category):
            cat_ls = split_comma(str_category)
            if set(cat_ls) - set(refseq_categories):
                raise ImportError(
                    f"refseq-category must be {','.join(refseq_categories)}"
                )
            else:
                return cat_ls

        def limit_parellel(n):
            n = int(n)
            max_task = 8
            if n > max_task:
                raise TypeError(f"maximum number of task is {max_task}")
            else:
                return n

        parser = argparse.ArgumentParser(
            formatter_class=ExplicitDefaultsHelpFormatter,
            description=f"{makura.__name__.capitalize()}: Download NCBI genomes",
        )
        parser.add_argument(
            "--version",
            "-v",
            action="version",
            version=f"{makura.__name__} {__version__}",
        )

        subcmd = parser.add_subparsers(
            dest="subcmd",
            description="subcommands",
            metavar="SUBCOMMAND",
        )

        update = subcmd.add_parser(
            "update",
            help="update assembly summary and taxonomy information",
            formatter_class=ExplicitDefaultsHelpFormatter,
        )

        update.add_argument(
            "--assembly-source",
            "-s",
            default="all",
            choices=["all", "refseq", "genbank"],
            help="Limit to 'refseq' (GCF_) or 'genbank' (GCA_) genomes",
        )

        download = subcmd.add_parser(
            "download",
            help="Download genomes from RefSeq or GenBank database",
            formatter_class=ExplicitDefaultsHelpFormatter,
        )
        download.add_argument(
            "--out_dir",
            "-o",
            help="output directory",
            type=parse_dir,
            default=Path().cwd(),
        )
        download.add_argument(
            "--update", "-U", help="update the assembly summary", action="store_true"
        )
        input_group = download.add_mutually_exclusive_group(required=True)
        input_group.add_argument(
            "--accessions",
            "-a",
            default=[],
            type=split_comma,
            help="Download by assembly accessions (comma-separated)",
        )
        input_group.add_argument(
            "--accession-list",
            help="Download by assembly accession list",
            type=check_file,
        )
        input_group.add_argument(
            "--taxids",
            "-t",
            default=[],
            type=split_comma,
            help="Download by taxid (comma-separated)",
        )
        input_group.add_argument(
            "--taxid-list", help="Download by taxid list", type=check_file
        )
        input_group.add_argument(
            "--groups",
            "-g",
            default=[],
            type=split_comma,
            help=f"""
                Limit to genomes at one or more groups (comma-separated)\n
                {','.join(groups)}
                """,
        )
        input_group.add_argument(
            "--microbiome", "-m", help="Download microbiome", action="store"
        )

        download.add_argument(
            "--assembly-level",
            "-l",
            default=[],
            type=check_levels,
            help=f"""Limit to genomes at one or more assembly levels (comma-separated)
            {','.join(asm_levels)}
            """,
        )

        download.add_argument(
            "--refseq-category",
            "-c",
            default=[],
            type=check_refseq_category,
            help=f"""
                Limit to genomes at one or more refseq category (comma-separated)\n
                {','.join(refseq_categories)}
                """,
        )

        download.add_argument(
            "--assembly-source",
            "-s",
            default="all",
            choices=["all", "refseq", "genbank"],
            help="Limit to 'refseq' (GCF_) or 'genbank' (GCA_) genomes",
        )

        download.add_argument(
            "--download-method",
            default="rsync",
            choices=["rsync", "https"],
            help="select the method for downloading genomes",
        )
        download.add_argument(
            "-p",
            "--parallel",
            dest="parallel",
            type=limit_parellel,
            default=4,
            help="Download genome with multiple processes (max: 8)",
        )
        download.add_argument(
            "--debug",
            action="store_true",
            help="Activate debug mode, it will output download_status.txt",
        )
        summary = subcmd.add_parser(
            "summary",
            formatter_class=ExplicitDefaultsHelpFormatter,
            help="Print a data report with genome metadata from RefSeq or GenBank database in JSON format",
        )
        summary.add_argument(
            "--update", "-U", help="update the assembly summary", action="store_true"
        )
        summary_input_group = summary.add_mutually_exclusive_group(required=True)
        summary_input_group.add_argument(
            "--accessions",
            "-a",
            default=[],
            type=split_comma,
            help="print records by assembly accessions (comma-separated)",
        )
        summary_input_group.add_argument(
            "--accession-list",
            help="print records by assembly accession list",
            type=check_file,
        )
        summary_input_group.add_argument(
            "--taxids",
            "-t",
            default=[],
            type=split_comma,
            help="print records by taxid (comma-separated)",
        )
        summary_input_group.add_argument(
            "--taxid-list", help="print records by taxid list", type=check_file
        )
        summary_input_group.add_argument(
            "--groups",
            "-g",
            default=[],
            type=split_comma,
            help=f"""
                Limit to genomes at one or more groups (comma-separated)\n
                {','.join(groups)}
                """,
        )
        summary_input_group.add_argument(
            "--microbiome",
            "-m",
            help="print records of microbiome",
            action="store_true",
        )

        summary.add_argument(
            "--assembly-level",
            "-l",
            default=[],
            type=check_levels,
            help=f"""Limit to genomes at one or more assembly levels (comma-separated)
            {','.join(asm_levels)}
            """,
        )

        summary.add_argument(
            "--refseq-category",
            "-c",
            default=[],
            type=check_refseq_category,
            help=f"""
                Limit to genomes at one or more refseq category (comma-separated)\n
                {','.join(refseq_categories)}
                """,
        )

        summary.add_argument(
            "--assembly-source",
            "-s",
            default="all",
            choices=["all", "refseq", "genbank"],
            help="Limit to 'refseq' (GCF_) or 'genbank' (GCA_) genomes",
        )
        summary.add_argument(
            "--as-json-lines",
            action="store_true",
            help="output assembly summary as jsonlines format",
        )
        api = subcmd.add_parser(
            "api",
            help="run RESTful API to get assembly summary",
            formatter_class=ExplicitDefaultsHelpFormatter,
        )
        api.add_argument(
            "--port", default=5000, type=str, help="which port to create API"
        )
        args = parser.parse_args()
        return args

    args = get_argument()
    if args.subcmd == "api":
        app.run(host="0.0.0.0", port=args.port)
        sys.exit(0)

    assembly_source = args.assembly_source
    asmsum = AssemblySummary()

    if args.subcmd == "update":
        if not asmsum.updated:
            asmsum.update_assembly_summary()
        sys.exit(0)

    refseq_category = args.refseq_category
    refseq_category = [
        f"{c} genome" if c in ("reference", "representative") else c
        for c in refseq_category
    ]

    assembly_level = args.assembly_level
    if args.accessions or args.accession_list:
        if args.accessions:
            accessions = args.accessions
        else:
            with open(args.accession_list, "r") as f:
                accessions = [
                    row.strip("\n ") for row in f.readlines() if row.strip("\n ")
                ]

    elif args.taxids or args.taxid_list:
        if args.taxids:
            taxids = args.taxids
        else:
            with open(args.taxid_list, "r") as f:
                taxids = [row.strip("\n ") for row in f.readlines() if row.strip("\n ")]

        accessions = asmsum.filter_accession_by_taxid(taxids=taxids)

    elif args.groups:
        accessions = asmsum.filter_accession_by_group(groups=args.groups)

    elif args.microbiome:
        accessions = asmsum.select_microbiome()

    else:
        accessions = []

    if len(accessions) > 0:
        if assembly_source == "genbank":
            accessions = [a for a in accessions if a.startswith("GCA_")]
        elif assembly_source == "refseq":
            accessions = [a for a in accessions if a.startswith("GCF_")]

        if refseq_category:
            accessions = asmsum.filter_refseq_category(
                accessions=accessions, categories=refseq_category
            )

        if assembly_level:
            accessions = asmsum.filter_assembly_level(
                accessions=accessions, levels=assembly_level
            )
    print(f"Number of assembly accession: {len(accessions)}", file=sys.stderr)
    if args.subcmd == "download":
        out_dir = args.out_dir
        parallel = args.parallel
        use_rsync = True if args.download_method == "rsync" else False
        debug = args.debug

        md5checksums_f = out_dir / "md5checksums.txt"
        if md5checksums_f.is_file():
            print(
                "uniq md5checksums.txt and remove genomes not in md5checksums.txt",
                file=sys.stderr,
            )
            asm_acc_regex = "GC[A|F]_[0-9]{9}\.[0-9]+"
            md5checksums_dct = dict(
                [
                    (re.search(asm_acc_regex, row)[0], row)
                    for row in md5checksums_f.read_text().split("\n")
                    if re.search(asm_acc_regex, row)
                ]
            )
            no_target = set(md5checksums_dct.keys()) - set(accessions)
            for asm_acc in no_target:
                md5checksums_dct.pop(asm_acc)
            md5checksums_f.write_text("\n".join(md5checksums_dct.values()) + "\n")

            removed = asmsum.check_genomes(md5checksums_f)
            if len(removed) > 0:
                print(f"Remove {len(removed)} genomes", file=sys.stderr)

        asmsum.download_by_accession(
            out_dir,
            accessions=accessions,
            use_rsync=use_rsync,
            parallel=parallel,
            debug=debug,
        )
    elif args.subcmd == "summary":
        out_fmt = "jsonlines" if args.as_json_lines else "tab"
        for row in asmsum.gen_summary(accessions=accessions, out_fmt=out_fmt):
            print(row, file=sys.stdout)
