# Generated by Django 5.1.1 on 2024-10-17 17:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('paid', models.DateTimeField(auto_now=True)),
                ('completed', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PD', 'pending'), ('CA', 'cancelled'), ('CD', 'completed')], default='PD', max_length=2)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_payment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-status'],
                'indexes': [models.Index(fields=['-status'], name='payment_tra_status_2dc573_idx')],
            },
        ),
    ]
