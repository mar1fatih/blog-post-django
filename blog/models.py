from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def published(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title