# Generated by Django 4.0.3 on 2023-01-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paint',
            name='is_recommended',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='paint',
            name='size_paint',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paint',
            name='tecnical',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
