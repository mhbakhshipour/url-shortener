import uuid

from django.db import models
from django.conf import settings


class Url(models.Model):
    creator = models.ForeignKey(
        "client.User", on_delete=models.CASCADE, related_name="creator_url")
    orginal_url = models.URLField()
    short_url_id = models.CharField(
        max_length=11, default=uuid.uuid4().hex[:6], unique=True)

    def __str__(self) -> str:
        return f"{self.creator.username}"
