# Generated by Django 5.0.6 on 2024-06-07 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_review_album'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
