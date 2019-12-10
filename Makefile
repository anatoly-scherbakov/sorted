system_python := $(shell which python3.7)

venv:
	virtualenv -p $(system_python) venv

develop: venv
	venv/bin/pip install -e .[dev]
