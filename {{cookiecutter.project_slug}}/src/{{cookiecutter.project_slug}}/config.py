import os

PROJECT_NAME = "{{ cookiecutter.project_name }}"
VECTOR_STORE = "{{ cookiecutter.vector_store }}"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "huggingface")