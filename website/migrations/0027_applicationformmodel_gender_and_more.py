# Generated by Django 4.1.5 on 2023-02-27 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_rename_dob_applicationformmodel_dateofbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformmodel',
            name='gender',
            field=models.CharField(default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='nationalIdOrPassport',
            field=models.FileField(null=True, upload_to='application/applicationIDorPassport'),
        ),
        migrations.AddField(
            model_name='applicationformmodel',
            name='workCertificate',
            field=models.FileField(null=True, upload_to='application/applicationWorkCertificate'),
        ),
        migrations.AlterField(
            model_name='applicationformmodel',
            name='cv',
            field=models.FileField(null=True, upload_to='application/applicationCV'),
        ),
    ]