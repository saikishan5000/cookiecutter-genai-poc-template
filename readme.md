# GenAI POC Cookiecutter Template

A reusable [cookiecutter](https://cookiecutter.readthedocs.io/) template for scaffolding small/POC-level AI or GenAI projects (RAG, agent, LLM pipeline, etc.) with a Streamlit UI — in one command, instead of building the folder structure by hand every time.

Pattern used: **Monorepo, separated layers** — UI (`app/`) calls into core logic (`src/`). Logic stays testable and reusable even if the UI is thrown away or replaced later.

---

## How to use this template

### 1. Install cookiecutter (one-time setup)

```bash
conda install -c conda-forge cookiecutter
```

### 2. Generate a new project from this template

```bash
cookiecutter https://github.com/your-username/genai-poc-template
```

(Or, if working from a local copy: `cookiecutter path/to/genai-poc-template`)

### 3. Answer the prompts

```
project_name (my_genai_poc): Resume JD Matcher
project_slug (resume_jd_matcher):        ← auto-filled, press Enter to accept
author_name (Kishan):                    ← press Enter to accept, or type a different name
description (A short one-line description of the project): RAG tool to match resume against JD
Select vector_store:
1 - chromadb
2 - faiss
Choose from 1, 2 (1): 1
```

- `project_name` — human-readable name, shown in README/UI titles
- `project_slug` — auto-generated, safe folder/package name (lowercase, underscores)
- `vector_store` — pick per project; installs the matching package automatically

### 4. A fully-scaffolded project folder is generated

```bash
cd resume_jd_matcher
conda env create -f environment.yml
conda activate resume_jd_matcher
streamlit run app/main.py
```

That's it — from zero to a running Streamlit app with the full folder structure, in under a minute.

---
## Optional: PowerShell shortcut
Add to $PROFILE:
function new-genai { cookiecutter https://github.com/saikishan5000/cookiecutter-genai-poc-template }

## What gets generated

```
project-name/
├── README.md
├── environment.yml            # conda environment definition
├── .env.example                # never commit actual .env
├── .gitignore
├── Makefile                    # shortcut commands: make run / make lint / make test
│
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── config.py            # settings, env var loading
│       ├── ingestion/           # data loading, chunking, parsing
│       ├── embeddings/          # embedding generation, vector store clients
│       ├── retrieval/           # retrievers, rerankers, hybrid search
│       ├── llm/                   # model clients, prompt templates, chains
│       ├── pipelines/           # orchestration (RAG pipeline, agent flows)
│       ├── evaluation/          # eval harness, metrics, test datasets
│       └── utils/
│
├── prompts/                     # versioned prompt templates (yaml/jinja)
│   └── v1/
│
├── app/                           # Streamlit UI — thin layer only
│   ├── main.py                    # entry point: streamlit run app/main.py
│   ├── pages/                     # multi-page app support (if needed)
│   ├── components/                # reusable UI widgets
│   └── state.py                   # session_state management helpers
│
├── .streamlit/
│   └── config.toml                # theme, server settings
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── eval/                        # golden datasets, regression tests
│
├── data/
│   ├── raw/
│   └── processed/
│
├── configs/                          # yaml configs per environment
│   ├── dev.yaml
│   └── prod.yaml
│
└── docs/
    └── architecture.md
```

---

## Core principles baked into this template

1. **UI stays thin, logic stays thick**
   `app/` only calls functions from `src/project_name/pipelines/`. No prompt construction, retrieval logic, or business logic inside Streamlit callbacks.

2. **Separate prompts from code**
   Prompts live as versioned files under `prompts/`, not hardcoded strings — enables iteration without redeploying code.

3. **Config-driven, not hardcoded**
   Model names, temperature, chunk sizes, top-k, etc. belong in `configs/*.yaml`, not scattered in code.

4. **Evaluation as a first-class citizen**
   `evaluation/` + `tests/eval/` hold golden datasets and metrics so changes to prompts/models don't silently degrade quality.

5. **Pipeline abstraction**
   Wrap stages (ingest → embed → retrieve → generate) as composable, testable functions/classes.

6. **Session state discipline (Streamlit-specific)**
   Centralize `st.session_state` logic in `app/state.py` instead of scattering checks across pages.

7. **Caching (Streamlit-specific)**
   Use `@st.cache_resource` for expensive one-time loads and `@st.cache_data` for data transforms.

8. **Secrets handling**
   Real secrets go in `.streamlit/secrets.toml` (gitignored) or environment variables — never committed.

9. **Data versioning**
   Avoid committing raw/large data directly; use DVC/Git LFS if data needs versioning.

---

## Mental model

```
UI (Streamlit: app/)
   → calls →
Pipelines (src/project_name/pipelines/)
   → calls →
Core logic (retrieval/, llm/, embeddings/, ingestion/)
```

If a project later needs an API or CLI, only a new entry point is added — no changes needed to retrieval/generation code, since the UI never contains logic directly.

---

## Standard tooling (pre-wired in the generated project)

- **Dependency management**: conda via `environment.yml`
- **Linting/formatting**: `ruff`
- **Testing**: `pytest`
- **Common commands**: `Makefile` (`make install`, `make run`, `make lint`, `make test`) — works on Linux/Git Bash/WSL; on plain Windows PowerShell, run the underlying commands directly

---

## When to move to a decoupled architecture

This monorepo pattern is right for POC/prototype scale. If a project generated from this template grows toward production:

- Move AI logic into a standalone backend service (e.g., FastAPI) with REST endpoints
- Streamlit (or any frontend) calls the backend over HTTP instead of importing code directly
- Enables independent scaling, secret isolation, and multiple frontends sharing one backend

```
backend/     # FastAPI serving AI logic, deployed independently
frontend/    # Streamlit/React, calls backend via HTTP
```

---

## Maintaining this template

- Template source lives in `{{cookiecutter.project_slug}}/` with variables defined in `cookiecutter.json`
- To test changes locally before pushing: `cookiecutter .` from the template root
- After confirming output looks correct (no leftover placeholder syntax in filenames/content), commit and push