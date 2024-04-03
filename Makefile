install:poetry.lock pyproject.toml
	poetry install
run: 
	@$(bash) echo "dont forget to run make run-server as well"
	poetry run python password_manager_gui/ui/main.py
format:
	poetry run ruff format password_manager_gui
lint:
	poetry run ruff check password_manager_gui
lint-fix:
	poetry run ruff check --fix password_manager_gui
lint-unsafe:
	poetry run check --fix --unsafe-fixes password_manager_gui
format-tests:
	poetry run ruff format tests/
lint-tests:
	poetry run ruff check tests/
lint-tests-fix:
	poetry run ruff check --fix tests/
lint-tests-unsafe:
	poetry run check --fix --unsafe-fixes tests/





run-server:
	poetry run uvicorn --app-dir password_manager_gui/backend server:app --reload