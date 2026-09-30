# Cookiecutter Django

A feature-rich, high-performance Django project template built with `uv`, modular app architecture, environment-based settings, Celery background task tracking, Pytest, Ruff, and Docker support.

## 🚀 Features

- **⚡ Fast Dependency Management**: Built on Astral's `uv` package manager with `pyproject.toml`.
- **🏗️ Scoped App Architecture**: Clean separation into `admin/`, `domain/`, `forms/`, `management/`, `models/`, `tasks/`, `templates/`, and `views/`.
- **⚙️ Environment-Based Settings**: Clean modular settings (`base.py`, `local.py`, `production.py`) with `django-environ`.
- **📊 Background Task Tracking**: Pre-configured Celery task lifecycle tracking (`BackgroundTask`, `BackgroundTaskEvent` models).
- **🗄️ Database Options**: Choose between PostgreSQL (`psycopg3`) or SQLite.
- **🐳 Docker Ready**: Optional multi-stage `Dockerfile`, `docker-compose.yml` (dev), and `docker-compose.production.yml` with Nginx reverse proxy.
- **🛡️ Code Quality & Sentry**: Pre-commit hooks with `ruff` and optional Sentry monitoring integration.
- **🐍 Automatic Venv Setup**: Automatically initializes a virtual environment named after your project (or `.venv`) using `uv venv` and installs all dependencies upon project generation.

---

## 💻 Usage

To create a new Django project using this template:

```bash
uvx cookiecutter /home/veera/Projects/cookiecutter-django
```

You will be prompted for:
1. **project_name**: e.g. `My Super App`
2. **project_slug**: e.g. `my_super_app`
3. **app_name**: e.g. `app`
4. **description**: Brief project summary
5. **author_name**: Your name
6. **email**: Your email address
7. **python_version**: Default `3.12`
8. **database**: Select `postgresql` or `sqlite`
9. **use_docker**: `y` or `n`
10. **use_sentry**: `y` or `n`
11. **use_precommit**: `y` or `n`
12. **venv_name**: Custom virtual environment name (defaults to `project_slug`)

---

## 📁 Project Structure Generated

```
<project_slug>/
├── app/                      # Main application
│   ├── admin/                # Django admin definitions
│   ├── domain/               # Core business domain logic & Celery event listeners
│   ├── forms/                # Django forms
│   ├── management/           # Custom management commands
│   ├── migrations/           # Database migrations
│   ├── models/               # Data models (BaseModel, BackgroundTask, etc.)
│   ├── tasks/                # Celery background tasks
│   ├── templates/            # HTML templates
│   └── views/                # Views & Controllers
├── config/                   # Project configuration
│   ├── settings/
│   │   ├── base.py           # Shared settings
│   │   ├── local.py          # Local development settings
│   │   └── production.py     # Production settings
│   ├── asgi.py
│   ├── celery.py
│   ├── urls.py
│   └── wsgi.py
├── docker/                   # Docker environment (Optional)
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.production.yml
│   └── nginx/
├── tests/                    # Pytest suite
│   ├── domain/
│   ├── mixins/
│   └── views/
├── .env.example              # Sample environment configuration
├── .gitignore
├── manage.py
├── pyproject.toml            # Project dependencies & config
└── SETUP.md                  # Generated project setup guide
```
