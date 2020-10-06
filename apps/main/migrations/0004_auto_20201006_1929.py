# Generated by Django 3.1.2 on 2020-10-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201006_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='original_url',
            field=models.URLField(verbose_name='Оригинальный URL'),
        ),
        migrations.AlterUniqueTogether(
            name='shorturl',
            unique_together={('user_id', 'original_url')},
        ),
    ]
