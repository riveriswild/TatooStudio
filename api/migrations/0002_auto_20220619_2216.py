# Generated by Django 3.1.7 on 2022-06-19 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('info', models.TextField(max_length=255)),
                ('telegram', models.CharField(max_length=124)),
                ('vk', models.CharField(max_length=124)),
                ('phone_number', models.CharField(max_length=14)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tatoo_image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Works',
            new_name='Work',
        ),
    ]
