# Generated by Django 4.2.7 on 2023-12-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_documentacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
    ]