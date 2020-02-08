# Generated by Django 3.0.2 on 2020-02-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_image', models.ImageField(blank=True, upload_to='image_photos', verbose_name='메인 이미지')),
                ('is_main', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
