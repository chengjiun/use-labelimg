#!/bin/bash
conda activate labelImg-tools
# annotation - epoch 2
DATADIR=./data/img2/
LABELDIR=./data/samples/labels-train1/
CLASSLIST=5classes.txt
cp $CLASSLIST $LABELDIR/classes.txt
python labelImg/labelImg.py $DATADIR $CLASSLIST $LABELDIR

