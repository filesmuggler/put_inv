# Generated by Django 2.2.5 on 2019-09-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('total_number', models.IntegerField()),
                ('used_number', models.IntegerField()),
            ],
        ),
    ]
