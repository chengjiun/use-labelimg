from pathlib import Path
import argparse
import sys

def main(argv):
    argparser = argparse.ArgumentParser(
        "remove txt files without jpg"
    )
    argparser.add_argument("path", nargs="?")
    args = argparser.parse_args(argv[1:])
    txt_files = [f for f in Path(args.path).glob('*.txt')]
    for f in txt_files:
        ff = f.name
        if ff == 'classes.txt':
            continue
        if not (f.parent / ff.replace('.txt','.jpg')).exists():
            f.unlink()

if __name__=='__main__':
    main(sys.argv)
