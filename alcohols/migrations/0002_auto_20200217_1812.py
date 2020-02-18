# Generated by Django 3.0.2 on 2020-02-17 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diaries', '0001_initial'),
        ('alcohols', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alcoholrecord',
            name='diary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alcohol_records', to='diaries.Diary'),
        ),
        migrations.AddField(
            model_name='alcohol',
            name='Alcohol_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alcohol', to='alcohols.AlcoholType'),
        ),
    ]