# Generated by Django 4.1.5 on 2023-02-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_rename_authorname_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('idOrPassport', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=255)),
                ('telephone', models.CharField(max_length=11)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('cv', models.FileField(upload_to='')),
                ('nationalIdOrPassport', models.FileField(upload_to='')),
                ('workCertificate', models.FileField(null=True, upload_to='')),
                ('refereeName', models.CharField(max_length=255)),
                ('refereeAddress', models.CharField(max_length=255)),
                ('refereeTelephone', models.CharField(max_length=11)),
                ('refereeInstitution', models.CharField(max_length=255)),
                ('refereeOccupation', models.CharField(max_length=255)),
            ],
        ),
    ]
