# Generated by Django 5.1.2 on 2024-10-16 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("link_tree", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="link",
            old_name="text",
            new_name="name",
        ),
    ]
