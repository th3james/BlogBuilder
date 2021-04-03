#!/usr/bin/env fish
python3 -m build
python3 -m pip uninstall blog-builder-th3james
python3 -m pip install blog-builder-th3james --no-index --find-links file://(pwd)/dist/blog_builder_th3james-0.0.1-py3-none-any.whl
