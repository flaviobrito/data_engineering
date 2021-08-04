
init:
	pip3 install -r requirements.txt

clean:
	rm -rf .venv
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

test:
	pytest -xv tests/tests_all.py

security:
	bandit -r . -x .venv -f csv -o ./security/out.csv

code_check:
	mypy ./module/* --exclude .venv --config-file  mypy.ini

postgres_build:
	docker build -t data_eng_postgresql .

postgres_compose:
	docker-compose up

postgres_run:
	docker run --rm -P --name pg_test data_eng_postgresql