# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

**Author:** {{ cookiecutter.author_name }}
**Vector store:** {{ cookiecutter.vector_store }}

## Setup

{% if cookiecutter.environment_manager == "conda" %}
\`\`\`bash
conda env create -f environment.yml
conda activate {{ cookiecutter.project_slug }}
\`\`\`
{% elif cookiecutter.environment_manager == "venv" %}
For Windows:
\`\`\`powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

For macOS/Linux:
\`\`\`bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
\`\`\`
{% endif %}

## Run

\`\`\`bash
streamlit run app/main.py
\`\`\`