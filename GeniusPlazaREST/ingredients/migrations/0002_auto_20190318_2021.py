# Generated by Django 2.1.7 on 2019-03-19 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient',
            new_name='ingredientName',
        ),
    ]
