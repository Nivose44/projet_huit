# Generated by Django 2.0.5 on 2018-05-20 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliments_manager', '0004_favorites_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='code',
            field=models.IntegerField(default='0122', max_length=15),
        ),
    ]
