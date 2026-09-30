# 🚀 {{ cookiecutter.project_name }} - Setup & Development Guide

Comprehensive instructions for setting up, running, testing, and deploying **{{ cookiecutter.project_name }}**.

---

## 📋 Prerequisites

- **Python**: `>= {{ cookiecutter.python_version }}`
- **uv**: Fast Python package installer ([Install uv](https://docs.astral.sh/uv/getting-started/installation/))
{% if cookiecutter.use_docker == 'y' %}- **Docker & Docker Compose**: For containerized execution{% endif %}

---

## 🛠️ Local Development Setup

### 1. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### 2. Activate Virtual Environment
```bash
source {{ cookiecutter.venv_name }}/bin/activate
```

### 3. Install Dependencies
```bash
uv sync --dev
```

{% if cookiecutter.use_docker == 'y' and cookiecutter.database == 'postgresql' %}
### 4. Start PostgreSQL & Redis Containers
```bash
docker compose -f docker/docker-compose.yml up -d db redis
```
{% endif %}

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Run Django Dev Server
```bash
python manage.py runserver 8000
```

### 7. Run Celery Worker (Separate Terminal Tab)
```bash
source {{ cookiecutter.venv_name }}/bin/activate
celery -A config worker -l info
```

---

{% if cookiecutter.use_docker == 'y' %}
## 🐳 Docker Setup

### Launch Development Stack
```bash
docker compose -f docker/docker-compose.yml up --build
```

### Launch Production Stack (With Nginx)
```bash
docker compose -f docker/docker-compose.production.yml up --build -d
```
{% endif %}

---

## 🧪 Testing & Code Quality

### Run Test Suite
```bash
uv run pytest
```

### Code Formatting & Linting
```bash
uv run ruff check .
uv run ruff format .
```
