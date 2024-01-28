# Generated by Django 4.2.7 on 2024-01-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcatgid', models.AutoField(primary_key=True, serialize=False)),
                ('catname', models.CharField(max_length=50)),
                ('subcatname', models.CharField(max_length=50, unique=True)),
                ('subcaticonname', models.CharField(max_length=100)),
            ],
        ),
    ]
