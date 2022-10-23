from django.db import models
from User.models import User
from django.db.models import Avg, Count


class Rate(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey('User.User', on_delete=models.CASCADE, null=False)
    content = models.ForeignKey('Content', on_delete=models.CASCADE, null=False)


class Content(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    @property
    def count_rate_users(self):
        return Rate.objects.filter(content=self).aggregate(Count('id'))

    @property
    def rate_avg(self):
        return Rate.objects.filter(content=self).aggregate(Avg('score'))



