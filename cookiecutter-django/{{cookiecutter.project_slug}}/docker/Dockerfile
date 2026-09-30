FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN python -m pip install --no-cache-dir uv

RUN uv sync --frozen || uv sync

COPY . .

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
