# Generated by Django 4.1.4 on 2024-02-07 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_remove_catalogue_seller_catalogue_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogue',
            old_name='product_image',
            new_name='product_image_1',
        ),
        migrations.RenameField(
            model_name='mastercatalogue',
            old_name='product_image',
            new_name='product_image_2',
        ),
        migrations.AddField(
            model_name='catalogue',
            name='product_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='product_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='product_image_4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='product_image_5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='mastercatalogue',
            name='product_image_1',
            field=models.ImageField(default=None, upload_to='master-images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mastercatalogue',
            name='product_image_3',
            field=models.ImageField(default=None, upload_to='master-images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mastercatalogue',
            name='product_image_4',
            field=models.ImageField(default=None, upload_to='master-images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mastercatalogue',
            name='product_image_5',
            field=models.ImageField(default=None, upload_to='master-images/'),
            preserve_default=False,
        ),
    ]
