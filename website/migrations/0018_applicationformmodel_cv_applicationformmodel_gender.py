# Generated by Django 4.1.5 on 2023-02-27 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_applicationformmodel_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformmodel',
            name='cv',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='gender',
            field=models.CharField(default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
