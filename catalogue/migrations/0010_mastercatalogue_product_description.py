# Generated by Django 4.1.4 on 2024-02-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_alter_catalogue_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mastercatalogue',
            name='product_description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
