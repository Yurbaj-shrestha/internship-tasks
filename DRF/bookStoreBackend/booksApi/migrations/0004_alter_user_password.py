# Generated by Django 5.1.6 on 2025-03-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksApi', '0003_remove_book_order_book_remove_book_order_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
