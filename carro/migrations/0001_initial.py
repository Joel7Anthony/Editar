# Generated by Django 4.1 on 2022-08-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('año', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=50)),
                ('chasis', models.CharField(max_length=50)),
                ('propietario', models.CharField(max_length=50)),
            ],
        ),
    ]
