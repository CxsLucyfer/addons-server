# Generated by Django 3.2.13 on 2022-05-31 10:43

from django.db import migrations


def delete_double_encoded_blogpost(apps, schema_editor):
    BlogPost = apps.get_model('devhub', 'BlogPost')
    # Delete double-encoded posts we've imported, the fixed cron will then
    # re-import them, unescaping wordpress content correctly before inserting
    # into the database.
    BlogPost.objects.filter(title__contains='&amp;').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('devhub', '0004_alter_blogpost_options'),
    ]

    operations = [migrations.RunPython(delete_double_encoded_blogpost)]
