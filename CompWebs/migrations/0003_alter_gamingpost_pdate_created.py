# Generated by Django 4.0.1 on 2022-03-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompWebs', '0002_alter_gamingpost_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamingpost',
            name='Pdate_Created',
            field=models.DateTimeField(),
        ),
    ]