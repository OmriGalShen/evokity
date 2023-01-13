.PHONY: lint format test

lint: **/*.py
	mypy evokity tests

check-format: **/*.pt
	black --check .

format: **/*.py
	black .

test: **/*.py
	pytest
