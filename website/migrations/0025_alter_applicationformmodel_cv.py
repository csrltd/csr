# Generated by Django 4.1.5 on 2023-02-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_remove_applicationformmodel_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformmodel',
            name='cv',
            field=models.FileField(upload_to='application/applicationImages'),
        ),
    ]
