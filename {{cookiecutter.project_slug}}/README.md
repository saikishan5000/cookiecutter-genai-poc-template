# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

**Author:** {{ cookiecutter.author_name }}
**Vector store:** {{ cookiecutter.vector_store }}

## Setup

\`\`\`bash
conda env create -f environment.yml
conda activate {{ cookiecutter.project_slug }}
\`\`\`

## Run

\`\`\`bash
streamlit run app/main.py
\`\`\`