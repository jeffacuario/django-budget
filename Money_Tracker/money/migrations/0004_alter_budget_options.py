# Generated by Django 3.2.6 on 2021-08-31 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0003_remove_budget_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budget',
            options={'ordering': ['-date']},
        ),
    ]
