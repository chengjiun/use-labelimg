#!/bin/bash
conda activate labelImg-tools
CLASSLIST=5classes.txt

# annotation - epoch 2
# DATADIR=./data/img2/
# LABELDIR=./data/samples/labels-train1/

# annotation - epoch 3
DATADIR=./data/samples/
LABELDIR=./data/samples-train2/labels
cp $CLASSLIST $LABELDIR/classes.txt
python labelImg/labelImg.py $DATADIR $CLASSLIST $LABELDIR



