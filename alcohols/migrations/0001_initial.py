# Generated by Django 3.0.2 on 2020-02-20 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='술이름')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AlcoholType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alcohol_name', models.CharField(max_length=100, verbose_name='술종류')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AlcoholRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bottles', models.FloatField()),
                ('glasses', models.FloatField()),
                ('alcohol_records', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alcohol_records', to='alcohols.Alcohol')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
