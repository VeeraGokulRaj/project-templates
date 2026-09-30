from django.apps import AppConfig


class {{ cookiecutter.project_name | replace(' ', '') | replace('_', '') | replace('-', '') }}Config(AppConfig):
    name = "{{ cookiecutter.app_name }}"

    def ready(self):
        import {{ cookiecutter.app_name }}.domain.background_task  # noqa: F401
