# Generated by Django 4.2.2 on 2023-07-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
