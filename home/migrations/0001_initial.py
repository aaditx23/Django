# Generated by Django 4.2.1 on 2023-06-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=11)),
                ('email', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
