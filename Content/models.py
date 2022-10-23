from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    @property
    def count_rate_users(self):
        return Rate.objects.filter(content=self).aggregate(Count('id'))

    @property
    def rate_avg(self):
        return Rate.objects.filter(content=self).aggregate(Avg('score'))



