Developer notes

- Run the main script: `python -m src.main`
- Created a minimal scaffold: `LICENSE`, `.gitignore`, `src/` package
- Next steps: add project-specific dependencies and tests

Python package manager

- Create a virtual environment and activate it:

	- `python -m venv .venv`
	- `source .venv/bin/activate`

- Install runtime dependencies:

	- `pip install -r requirements.txt`

- Install development dependencies:

	- `pip install -e .[dev]`

- Helpful commands:

	- `python -m pip install --upgrade pip`
	- `python -m pytest`  # run tests
	 - `tox`  # run tests in a tox env

	Pre-commit

	- Install pre-commit hooks locally:

		- `pre-commit install`

	- Run pre-commit on all files:

		- `pre-commit run --all-files`
