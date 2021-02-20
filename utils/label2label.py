"""
translate label index in yolo format files from class1.txt to class2.txt
"""
import argparse
from pathlib import Path
import sys


def readYolofile(file):
    with open(file, "r") as f:
        txt = f.readlines()
    parsed = [(l.split()[0], " ".join(l.split()[1:])) for l in txt]
    return parsed


def writeYolofile(file, parsed):
    lines = [" ".join([t[0], t[1] + "\n"]).replace("\n\n", "\n") for t in parsed]

    with open(file, "w") as f:
        f.writelines(lines)


def read_classes(class_file):
    with open(class_file, "r") as f:
        classes = [c.replace("\n", "") for c in f.readlines()]

    return classes


def generate_id_refDict(ori_class_file, target_class_file):
    fromClasses = read_classes(ori_class_file)
    toClasses = read_classes(target_class_file)
    refDict = {}
    for i, c in enumerate(fromClasses):
        if c in toClasses:
            j = toClasses.index(c)
            refDict[i] = j
    return refDict


def label2label(labelfile, id_refDict, extra_id_ref=None, output=None):
    yolo_parsed = readYolofile(labelfile)
    target_lines = []
    for lines in yolo_parsed:
        oriLabel = int(lines[0])
        if oriLabel in id_refDict:
            targetLabel = id_refDict[oriLabel]
        elif extra_id_ref is not None and oriLabel in extra_id_ref:
            targetLabel = extra_id_ref[oriLabel]
        else:
            targetLabel = oriLabel
        if targetLabel is not None:
            target_lines.append((str(targetLabel), lines[1]))
    if output is None:
        output = labelfile
    print(f"processed files to {output}")
    writeYolofile(output, target_lines)


EXTRA_ID_REF = {i0: 2 for i0 in range(1, 90)}
IGNORE_ID_REF = {94: None}
EXTRA_ID_REF = {**EXTRA_ID_REF, **IGNORE_ID_REF}


def main(argv):
    argparser = argparse.ArgumentParser(
        "translate labelId in Yolo format file form ori_class to target_class"
    )
    argparser.add_argument("labelpath", nargs="?")
    argparser.add_argument("ori_classes_file", nargs="?")
    argparser.add_argument("target_classes_file", nargs="?")
    argparser.add_argument("outputPath", default=None, nargs="?")
    args = argparser.parse_args(argv[1:])
    print(f"args: {args}")
    labelfiles = [p for p in Path(args.labelpath).glob("*.txt")]
    id_refDict = generate_id_refDict(args.ori_classes_file, args.target_classes_file)
    outputPath = Path(args.outputPath)
    if outputPath is None:
        outputPath = Path(args.labelpath)
    outputPath.mkdir(exist_ok=True)
    for labelfile in labelfiles:
        outputfile = outputPath / labelfile.name
        if labelfile.name == "classes.txt":
            continue
        try:
            label2label(
                str(labelfile),
                id_refDict,
                extra_id_ref=EXTRA_ID_REF,
                output=str(outputfile),
            )
        except ValueError as err:
            print(f"labelfile: {labelfile}")
            raise err


if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv)