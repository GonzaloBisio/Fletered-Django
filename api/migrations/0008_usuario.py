# Generated by Django 4.2.7 on 2023-12-03 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_conductor_imagen_conductor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('dni', models.CharField(max_length=20)),
                ('firebase_id', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
