from django.db import models
from .account import Account
from webhook.config import HttpMethodChoices

class Destination(models.Model):
    """Holds the Destination Details for accounts."""

    account = models.ForeignKey(Account, related_name='related_account_destinations', on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=10, choices=HttpMethodChoices.choices)
    headers = models.JSONField()