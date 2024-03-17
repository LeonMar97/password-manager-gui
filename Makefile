install:poetry.lock pyproject.toml
	poetry install
run:
	poetry run python main.py