# Generated by Django 3.1.1 on 2020-09-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200924_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Yorum'),
        ),
    ]