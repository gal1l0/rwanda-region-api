# Generated by Django 2.2.12 on 2020-08-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=40)),
                ('district', models.CharField(max_length=40)),
                ('sector', models.CharField(max_length=40)),
                ('cell', models.CharField(max_length=40)),
                ('village', models.CharField(max_length=40)),
            ],
        ),
    ]