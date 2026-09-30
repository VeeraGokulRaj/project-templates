from {{ cookiecutter.app_name }}.models import BackgroundTask


class BackgroundTaskMixin:
    @staticmethod
    def create_background_task(task_id="test-task-1", name="test_task", **kwargs):
        return BackgroundTask.objects.create(
            task_id=task_id,
            name=name,
            **kwargs,
        )
