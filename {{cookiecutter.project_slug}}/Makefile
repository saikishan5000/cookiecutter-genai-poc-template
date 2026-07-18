.PHONY: install run lint test clean

install:
{% if cookiecutter.environment_manager == "conda" %}
	conda env create -f environment.yml
{% elif cookiecutter.environment_manager == "venv" %}
	python -m venv .venv
	.venv/Scripts/pip install -r requirements.txt || .venv/bin/pip install -r requirements.txt
{% endif %}

run:
	streamlit run app/main.py

lint:
	ruff check --fix .
	ruff format .

test:
	pytest tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +