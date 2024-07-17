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

check:
	poetry run flake8 gendiff
	poetry run flake8 tests
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

all_pack:
	make build
	make publish
	make package-install