from django.db import models
from django.utils import timezone


class Post(models.Model):
#    author = models.ForeignKey('auth.User')
#    posts1 = open('buf.txt').read()
    title = models.CharField(max_length=200)
    text = models.TextField()
    text = 'ggggggg'
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
