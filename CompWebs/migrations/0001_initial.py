# Generated by Django 4.0.1 on 2022-03-08 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GamingTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_Title', models.CharField(max_length=250)),
                ('Tdate_Created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GamingPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pdate_Created', models.DateTimeField(default=django.utils.timezone.now)),
                ('Post_Content', models.CharField(default='stuffman', max_length=99999)),
                ('Post_Topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CompWebs.gamingtopic')),
                ('author', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
