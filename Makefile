install:
	poetry install

test:
	poetry run pytest

build:
	poetry build

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall
