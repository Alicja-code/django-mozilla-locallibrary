# Generated by Django 3.1.7 on 2021-04-07 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210407_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
