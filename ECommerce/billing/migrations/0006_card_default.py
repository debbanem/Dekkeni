# Generated by Django 2.2.1 on 2019-06-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_card_card_holder_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='default',
            field=models.BooleanField(default=True),
        ),
    ]