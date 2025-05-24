# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Setup

This repository requires:
- Poetry for Python dependency management: `pipx install poetry`
- Databricks CLI: `brew install databricks`
- Volta for Node.js tools: `brew install volta`
- Claude Code: `volta install @anthropic-ai/claude-code`

## Project Structure

This is a Databricks Asset Bundle project for a DB RAG pipeline:
- `databricks.yml` - Main bundle configuration
- `resources/` - Databricks resource definitions (jobs, clusters, etc.)
- `src/db_rag/` - Python package with pipeline tasks
- `.github/workflows/` - CI/CD pipeline for deployment

## Common Commands

- Install dependencies: `poetry install`
- Run linting: `poetry run black src/ && poetry run isort src/ && poetry run flake8 src/`
- Run tests: `poetry run pytest`
- Validate bundle: `databricks bundle validate`
- Deploy bundle: `databricks bundle deploy`

## Architecture

The RAG pipeline consists of three main tasks:
1. Data ingestion (`src/db_rag/tasks/ingest.py`)
2. Embeddings processing (`src/db_rag/tasks/embeddings.py`) 
3. Vector index creation (`src/db_rag/tasks/vector_index.py`)

Tasks are orchestrated via Databricks Jobs defined in `resources/jobs.yml`.