# Generated by Django 4.2.4 on 2023-08-21 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_appuser_contacts_appuser_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='contacts',
            field=models.ManyToManyField(related_name='contacts_related', through='user.Contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='moves',
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.IntegerField(default=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('from_user', 'to_user')},
            },
        ),
        migrations.AddField(
            model_name='appuser',
            name='moves',
            field=models.ManyToManyField(related_name='moves_related', through='user.Move', to=settings.AUTH_USER_MODEL),
        ),
    ]