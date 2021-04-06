#!/usr/bin/env fish
python3 -m build
python3 -m pip uninstall blog-builder-th3james
python3 -m pip install -e .
