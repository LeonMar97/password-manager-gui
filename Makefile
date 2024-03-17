install:poetry.lock pyproject.toml
	@pip install poetry && poetry install
run:
	@poetry run python main.py