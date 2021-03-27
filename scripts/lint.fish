#!/usr/bin/env fish
flake8 src/blogbuilder
black --check src/blogbuilder
mypy src/blogbuilder
