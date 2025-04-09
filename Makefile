PYTHON=python3

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  format             - Format code"
	@echo "  lint               - Check code quality and formattings"
	@echo "  typecheck          - Static type checking in strict mode"
	@echo "  test               - Run tests"
	@echo "  test-record        - Record tests"
	@echo "  test-diff [FILE]   - Diff tests"
	@echo "  py2c               - Convert Python to C"
	@echo "  config2bin         - Convert config to binary"
	@echo "  dev                - Run development environment"
	@echo "  build              - Build the project"
	@echo "  install            - Install the project"
	@echo "  help               - Show this help message"
	@echo ""
	@echo "Radon Software Foundation - https://radon-project.github.io/"

.PHONY: format
format:
	@isort . --quiet
	@ruff format .

.PHONY: lint
lint:
	@ruff format --check .
	@ruff check .

.PHONY: typecheck
typecheck:
	@mypy . --strict

.PHONY: test
test:
	@$(PYTHON) test.py full

.PHONY: test-record
test-record:
	@$(PYTHON) test.py record

.PHONY: test-diff
test-diff:
	@$(PYTHON) test.py diff $(word 2,$(MAKECMDGOALS))

.PHONY: py2c
py2c:
	@# Need to test it.
	@echo "Command in development"
	@# $(PYTHON) -m cython -3 -a radon.py -o radon.c --embed -I/usr/include/python3.11

.PHONY: config2bin
config2bin:
	@echo "Command in development"

.PHONY: dev
dev:
	@echo "Running development requirements installation"
	@$(PYTHON) -m pip install -r requirements-dev.txt
	@echo "Running development tests"
	@$(PYTHON) test.py full

.PHONY: build
build:
	@echo "Command in development"

.PHONY: install
install:
	@echo "Command in development"
