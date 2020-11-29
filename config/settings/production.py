import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *


# Configuration for products dowload
PRODUCT_CLIENT_PAGE_SIZE = 1000
PRODUCT_CLIENT_NUMBER_OF_PAGES = 10

# Sentry configuration
sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)