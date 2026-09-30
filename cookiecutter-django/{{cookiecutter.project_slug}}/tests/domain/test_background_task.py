import pytest
from {{ cookiecutter.app_name }}.models import BackgroundTask, TaskStatus


@pytest.mark.django_db
def test_background_task_creation():
    task = BackgroundTask.objects.create(
        task_id="task-123",
        name="test_task",
        status=TaskStatus.PENDING,
    )
    assert task.task_id == "task-123"
    assert task.status == TaskStatus.PENDING
    assert str(task) == "test_task [task-123]"
