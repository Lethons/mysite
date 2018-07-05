from datetime import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    tag = models.CharField(max_length=10)

    def __str__(self):
        return self.tag


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = RichTextUploadingField()
    publish_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='blog/%Y/%m/%d')
    is_commend = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']
