install:poetry.lock pyproject.toml
	poetry install
run: 
	@$(bash) echo "dont forget to run make run-server as well"
	poetry run python main.py
format:
	poetry run ruff format .
lint:
	poetry run ruff check .
lint-fix:
	poetry run ruff check --fix 
lint-unsafe:
	poetry run check --fix --unsafe-fixes
run-server:
	poetry run uvicorn --app-dir backend server:app --reload	