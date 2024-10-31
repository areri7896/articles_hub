from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Transaction(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PD', 'pending'
        CANCELLED = 'CA', 'cancelled'
        COMPLETED = 'CD', 'completed'

    phone = models.IntegerField()
    amount = models.IntegerField()
    # title = models.CharField(max_length=250)
    # buyer = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name='article_payment'
    #     )
    paid = models.DateTimeField(auto_now=True)
    completed = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.PENDING
        )
    def get_absolute_url(self):
        return reverse('payment', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-status']
        indexes = [
            models.Index(fields=['-status']),
            ]

    # def __str__(self):
    #     return self.buyer
