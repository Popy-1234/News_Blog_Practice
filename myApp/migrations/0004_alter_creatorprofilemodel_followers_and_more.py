# Generated by Django 5.1.2 on 2024-10-21 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_creatorprofilemodel_achievements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorprofilemodel',
            name='Followers',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viewersprofilemodel',
            name='Followers',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
