# Generated by Django 3.0.2 on 2020-03-04 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0003_auto_20200223_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alcohol',
            name='Alcohol_type',
        ),
        migrations.RemoveField(
            model_name='alcoholrecord',
            name='alcohol_records',
        ),
        migrations.AddField(
            model_name='alcohol',
            name='alcohol_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alcohol_type', to='alcohols.AlcoholType'),
        ),
        migrations.AddField(
            model_name='alcoholrecord',
            name='alcohol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alcohol', to='alcohols.Alcohol'),
        ),
        migrations.AlterField(
            model_name='alcoholtype',
            name='alcohol_name',
            field=models.CharField(max_length=20),
        ),
    ]
