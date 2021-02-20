#!/bin/bash
conda activate labelImg-tools
python labelImg/labelImg.py ./data/val1 ./5classes.txt ./data/val1/
