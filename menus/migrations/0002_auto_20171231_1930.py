# Generated by Django 2.0 on 2017-12-31 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='content',
            new_name='contents',
        ),
    ]