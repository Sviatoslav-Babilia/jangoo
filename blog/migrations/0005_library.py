# Generated by Django 3.1.7 on 2021-04-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210404_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.IntegerField(max_length=13)),
            ],
        ),
    ]
