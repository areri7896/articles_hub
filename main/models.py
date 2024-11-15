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


class MPesaTransaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mpesa_transactions"
    )
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="Pending")
    transaction_date = models.DateTimeField(null=True, blank=True)
    mpesa_receipt_number = models.CharField(max_length=255,null=True, blank=True, unique=True )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.phone_number} - {self.amount} KES"



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    article = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="article_comments")
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_list')