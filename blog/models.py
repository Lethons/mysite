from django.db import models
from datetime import datetime


class Tag(models.Model):
    tag = models.CharField(max_length=10)

    def __str__(self):
        return self.tag


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    publish_time = models.DateField(default=datetime.now)
    update_time = models.DateField(auto_now=True)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='blog/%Y/%m/%d')
    is_commend = models.BooleanField(default=False)

    def __str__(self):
        return self.title
