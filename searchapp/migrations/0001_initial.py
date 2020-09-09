# Generated by Django 3.1.1 on 2020-09-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='India',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officename', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('officetype', models.CharField(max_length=3)),
                ('deliverystatus', models.CharField(max_length=12)),
                ('divisionname', models.CharField(max_length=23)),
                ('regionname', models.CharField(max_length=23)),
                ('circlename', models.CharField(max_length=16)),
                ('taluk', models.CharField(max_length=42)),
                ('districtname', models.CharField(max_length=24)),
                ('statename', models.CharField(max_length=25)),
                ('stateshort', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'india',
            },
        ),
    ]