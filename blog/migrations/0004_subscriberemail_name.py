# Generated by Django 4.1.2 on 2022-10-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_delete_coursecategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscriberemail",
            name="name",
            field=models.CharField(default="suman", max_length=100),
            preserve_default=False,
        ),
    ]
