# Generated by Django 4.1.6 on 2023-02-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.JSONField(default=dict),
        ),
    ]
