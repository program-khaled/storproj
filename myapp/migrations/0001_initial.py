# Generated by Django 4.2 on 2023-04-17 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('desc', models.CharField(max_length=1500)),
                ('image', models.FilePathField()),
            ],
        ),
    ]
