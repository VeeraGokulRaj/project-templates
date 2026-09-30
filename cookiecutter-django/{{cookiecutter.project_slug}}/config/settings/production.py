"""
Production settings for {{ cookiecutter.project_name }} project.
"""

from .base import *  # noqa: F403
from .base import SITE_URL, env
{% if cookiecutter.use_sentry == 'y' %}
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
{% endif %}

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
X_FRAME_OPTIONS = "DENY"
USE_X_FORWARDED_HOST = True

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=[SITE_URL],
)

{% if cookiecutter.use_sentry == 'y' %}
SENTRY_DSN = env("SENTRY_DSN", default="")
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
            CeleryIntegration(),
        ],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
{% endif %}
