SHELL=/usr/bin/env bash

install:
	pip install pip-tools
	pip-sync requirements.txt
	pip install .

install-dev:
	pip install pip-tools
	pip-sync requirements.txt requirements-dev.txt
	pip install -e .

pin:
	pip-compile requirements.in -o requirements.txt
	pip-compile requirements-dev.in -o requirements-dev.txt

pysen-configure:
	pysen generate .

lint:
	pysen run lint

format:
	pysen run format

test:
	pytest tests/

.PHONY:
	install install-dev pin pysen-configure lint format test
