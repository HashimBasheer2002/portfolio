# Generated by Django 5.1.7 on 2025-04-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='experience_logos/')),
            ],
        ),
    ]
