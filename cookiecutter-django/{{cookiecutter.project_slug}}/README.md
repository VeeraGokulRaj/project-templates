# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## 🚀 Quick Start

1. **Copy Environment Configuration**
   ```bash
   cp .env.example .env
   ```

2. **Activate Virtual Environment**
   ```bash
   source {{ cookiecutter.venv_name }}/bin/activate
   ```

3. **Run Migrations & Start Server**
   ```bash
   python manage.py migrate
   python manage.py runserver 8000
   ```

For detailed instructions including Docker setup, testing, and Celery worker execution, see [SETUP.md](SETUP.md).
