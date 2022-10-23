from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

