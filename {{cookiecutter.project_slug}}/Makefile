.PHONY: install run lint test clean

install:
	conda env create -f environment.yml

run:
	streamlit run app/main.py

lint:
	ruff check --fix .
	ruff format .

test:
	pytest tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +