# Generated by Django 3.2.6 on 2021-09-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0009_alter_card_cardname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardName',
            field=models.CharField(max_length=20, verbose_name='Card Name/Bank Account'),
        ),
    ]
