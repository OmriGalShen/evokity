.PHONY: lint format test check-format

lint: **/*.py
	mypy evokity tests

check-format: **/*.py
	black --check .

format: **/*.py
	black .

test: **/*.py
	pytest
