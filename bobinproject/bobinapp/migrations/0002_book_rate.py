# Generated by Django 4.2.9 on 2024-07-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bobinapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
