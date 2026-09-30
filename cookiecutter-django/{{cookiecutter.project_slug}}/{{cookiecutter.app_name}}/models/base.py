from model_utils.models import TimeStampedModel
from safedelete.models import SOFT_DELETE_CASCADE, SafeDeleteModel
from simple_history.models import HistoricalRecords


class BaseModel(SafeDeleteModel, TimeStampedModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

    @classmethod
    def list_permissions(cls):
        default_permissions = ["add", "change", "delete", "view"]
        model_name = cls._meta.model_name
        default_permission_codenames = [
            f"{perm}_{model_name}" for perm in default_permissions
        ]
        custom_permissions = getattr(cls._meta, "permissions", [])
        custom_permission_codenames = [perm[0] for perm in custom_permissions]
        return default_permission_codenames + custom_permission_codenames
