import uuid
from django.db import models

class Account(models.Model):
    """Holds the Account Details"""

    email = models.EmailField(unique=True)
    account_id = models.CharField(max_length=50, unique=True)
    account_name = models.CharField(max_length=100)
    app_secret_token = models.UUIDField(default=uuid.uuid4, editable=False)
    website = models.URLField(blank=True, null=True)
