from pathlib import Path
import argparse
import sys


def main(argv):
    argparser = argparse.ArgumentParser("check missing txt files")
    argparser.add_argument("path", nargs="?")
    args = argparser.parse_args(argv[1:])
    jpg_files = [f.name.replace(".jpg", "") for f in Path(args.path).glob("*.jpg")]
    txt_files = [f.name.replace(".txt", "") for f in Path(args.path).glob("*.txt")]
    missing_txt = [jpgf for jpgf in jpg_files if jpgf not in txt_files]
    missing_jpg = [txtf for txtf in txt_files if txtf not in jpg_files]
    print("---------- missing TXT files ----------")
    for m in missing_txt:
        print(Path(args.path) / (m + ".txt"))
    print("---------- missing JPG files ----------")
    for m in missing_jpg:
        print(Path(args.path) / (m + ".jpg"))


if __name__ == "__main__":
    main(sys.argv)
