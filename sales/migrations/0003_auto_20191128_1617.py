# Generated by Django 2.2.7 on 2019-11-28 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_sale_blog_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='blog_views',
            new_name='view_count',
        ),
    ]
