install:poetry.lock pyproject.toml
	poetry install
run:
	poetry run python main.py
format:
	poetry run ruff format .
lint:
	poetry run ruff check .
lint-fix:
	poetry run ruff check --fix 
lint-unsafe:
	poetry run check --fix --unsafe-fixes