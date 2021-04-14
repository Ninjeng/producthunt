# Generated by Django 3.2 on 2021-04-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comments_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='product',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
