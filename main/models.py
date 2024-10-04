from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=50)
    description =models.TextField()
    updated =models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='images/articles_uploads')

    def __str__(self):
        return self.title