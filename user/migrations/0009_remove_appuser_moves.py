# Generated by Django 4.2.4 on 2023-08-21 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_move_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='moves',
        ),
    ]
