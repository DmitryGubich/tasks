shell := uv run

.PHONY: pre-commit
pre-commit:
	$(shell) pre-commit run --all-files

.PHONY: run-tests
run-tests:
	$(shell) pytest