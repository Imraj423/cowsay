# Generated by Django 3.0.3 on 2020-02-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowsay', '0003_delete_historicalcow'),
    ]

    operations = [
        migrations.AddField(
            model_name='cow',
            name='history',
            field=models.TextField(default=models.TextField(max_length=30)),
        ),
    ]
