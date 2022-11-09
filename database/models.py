from django.db import models


# Create your models here.

class Account(models.Model):
    account_id = models.BigIntegerField(unique=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=True)
    account_name = models.CharField(max_length=255, blank=True)
    app_secret_token = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return '%s, %s' % (self.email, self.account_name)


class Destination(models.Model):
    account_id = models.BigIntegerField(blank=True, null=True)
    urls = models.URLField(max_length=255, blank=True)
    http_methods = models.CharField(max_length=255, blank=True)
    headers = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return '%s' % self.urls
