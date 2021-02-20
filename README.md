# A Note to use labelImg
- see https://github.com/tzutalin/labelImg.git

## modification of labelImg
1. ignore classes in the label txt file if its classIndex exceed the label list. This is helpful to pre-annotate COCO classes with pretrained models, and then remove the unnecessary labels. 

## environment setup

- use conda_install_labelImgtools.sh

# AUX

## view tab

- autosaving mode
- advanced mode

## shortcut

- check labelImg.py 
- next/previous image: d / a
- zoom in / out: Ctrl+ / Ctrl-
- zoom to original size: Ctrl=
- create new box: w
- delete box: Delete
- delete image: Ctrl Shift d 

# execuation
- put data to ./data/images\
- class list (coco80.txt) in ./
```
python labelImg/labelImg.py ./data/images ./coco80.txt ./data/label
```
