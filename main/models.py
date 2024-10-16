from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Article(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        UPDATED = 'UP', 'Updated'

    title = models.CharField(max_length=250)
    body =models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='article_posts'
        )
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='docs/articles_uploads')
    slug = models.SlugField(max_length=250)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
        )
    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
            ]

    def __str__(self):
        return self.title