# Generated by Django 5.1.1 on 2024-11-05 11:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_article_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MPesaTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('mpesa_receipt_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpesa_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
