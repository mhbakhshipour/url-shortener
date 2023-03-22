import uuid

from django.db import models
from django.conf import settings


class Url(models.Model):
    creator = models.ForeignKey(
        "client.User", on_delete=models.CASCADE, related_name="creator_url")
    orginal_url = models.URLField()
    short_url = models.URLField()

    def __str__(self) -> str:
        return f"{self.creator.username}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if is_new and not self.short_url:
            self.short_url = "{}/{}".format(settings.BASE_URL,
                                            uuid.uuid4().hex[:6])

        return super(Url, self).save(*args, **kwargs)
