# Generated by Django 4.1.7 on 2023-02-26 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_category_alter_product_category_delete_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categoryall',
        ),
    ]
