#!/usr/bin/env fish
flake8 blogbuilder
black --check blogbuilder
mypy blogbuilder