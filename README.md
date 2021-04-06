# Blog builder

Personal static blog builder

## Usage

```shell
blogbuilder blog/posts/ blog/templates/ blog/output_dir
```

## Dev scripts

```shell
# Activate venv - do this first, per shell
source .venv/bin/activate.fish

# Install
scripts/./install.fish

# Lint
scripts/./lint.fish

## Run tests
scripts/./run-tests.fish

## Install blogbuilder pip egg as editable install
scripts/./install-pip-editable.fish
## Install blogbuilder pip package as built package
scripts/./install-pip-release.fish
```
