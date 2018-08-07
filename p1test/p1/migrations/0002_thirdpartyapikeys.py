# Generated by Django 2.0.7 on 2018-08-06 20:07

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdPartyApiKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=30)),
                ('api_url', models.CharField(max_length=100)),
                ('api_key', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
            ],
        ),
    ]