# Generated by Django 4.1.3 on 2022-11-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paraplan', models.CharField(max_length=50)),
                ('podveska', models.CharField(max_length=30)),
            ],
        ),
    ]