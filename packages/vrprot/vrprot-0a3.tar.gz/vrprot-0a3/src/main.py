#! python3

from vrprot.alphafold_db_parser import AlphafoldDBParser
from vrprot.argument_parser import argument_parser
from vrprot.classes import Logger
import os

log = Logger("main")
WD = os.path.dirname(os.path.abspath(__file__))


def main(args=None):
    """Main function will take the arguments passed by the user and execute the program accordingly."""
    if args is None:
        args = argument_parser().parse_args()
    parser = AlphafoldDBParser()
    processing_files = os.path.join(WD, "processing_files")
    maps = os.path.join(processing_files, "MAPS")
    parser.update_output_dir(maps)
    if args.mode == "clear":
        parser.clear_default_dirs()
        exit()
    parser.set_all_arguments(args)
    if args.mode == "fetch":
        parser.execute_fetch(args.proteins[0])
    if args.mode == "local":
        parser.execute_local(args.source)
    if args.mode == "list":
        with open(args.file[0]) as f:
            proteins = f.read().splitlines()
        parser.execute_from_object(proteins)
    if args.mode == "bulk":
        parser.execute_from_bulk(args.source)
    if args.mode == "extract":
        parser.extract_archive(args.archive)
    if args.mode == "combine":
        parser.execute_apply_to_multifractions()


if __name__ == "__main__":
    main()
