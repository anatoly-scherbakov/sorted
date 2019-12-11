.PHONY: clean develop pypi

system_python := $(shell which python3.7)

venv:
	virtualenv -p $(system_python) venv

develop: venv
	venv/bin/pip install -e .[dev]

clean:
	rm -rf build dist *.egg-info .pytest_cache

dist: venv
	venv/bin/python setup.py sdist bdist_wheel

pypi: dist
	venv/bin/twine upload dist/*
