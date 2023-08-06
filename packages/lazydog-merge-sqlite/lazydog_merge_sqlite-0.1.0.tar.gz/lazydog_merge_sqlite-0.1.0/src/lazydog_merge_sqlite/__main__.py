# SPDX-License-Identifier: EUPL-1.2
import argparse
import logging
from pathlib import Path
from typing import List
from lazydog_merge_sqlite import merge_sqlite

logger = logging.getLogger("lazydog_merge_main")


def check_db_files(db_files: List[Path]):
    """Check if a list of paths point to existing files on disk"""
    for dbfile in db_files:
        if not dbfile.exists():
            logger.error(f"File {dbfile} does not exist and can't be loaded")
            exit(1)
        if not dbfile.is_file():
            logger.error(f"File {dbfile} is not a file can't be loaded")
            exit(1)


def main():
    parser = argparse.ArgumentParser(
        prog="lazydog_merge_sqlite",
        description="Merge Sqlite DB files even when they have different tables",
    )
    parser.add_argument(
        "db_files",
        metavar="N",
        nargs="+",
        help="list of existing DB files to merge",
        type=Path,
    )
    parser.add_argument("--out", help="Output DB to write to", type=Path)
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Write more output"
    )
    args = parser.parse_args()
    if args.verbose:
        log_level = "DEBUG"
    else:
        log_level = "INFO"
    logging.basicConfig(
        format="%(asctime)s %(name)s %(levelname)s: %(message)s", level=log_level
    )
    check_db_files(args.db_files)

    if args.out is None:
        if len(args.db_files) == 1:
            logger.warn("Can't merge anything for a single file")
            exit(0)
        merge_sqlite.sql_merge_dbs(args.db_files[1:], args.db_files[0])

    else:
        dst: Path = args.out
        if dst.exists():
            if not dst.is_file():
                logger.error("Output location already exists and isn't a file")
                exit(1)
            merge_sqlite.sql_merge_dbs(args.db_files, dst)
        else:
            merge_sqlite.first_copy(args.db_files[0], dst)
            merge_sqlite.sql_merge_dbs(args.db_files[1:], dst)


if __name__ == "__main__":
    main()
