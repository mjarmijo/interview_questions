install:
	poetry install

format:
	poetry run ruff format

test:
	poetry run pytest --cov=log_analysis tests/

.PHONY: install format test