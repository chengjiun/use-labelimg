## environment setup
```
sudo apt-get install pyqt5-dev-tools
conda create -n labelImg-tools -c conda-forge python=3.7
conda activate labelImg-tools
git clone https://github.com/tzutalin/labelImg.git
cd labelImg
pip install -r requirements/requirements-linux-python3.txt
make qt5py3
python3 labelImg.py
```

# Note
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
