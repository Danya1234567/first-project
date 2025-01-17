# Generated by Django 4.2.16 on 2024-11-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/technique')),
                ('type', models.CharField(choices=[('Cars', 'Cars'), ('Motorcycles', 'Motorcycles'), ('Flat', 'Flat'), ('House', 'House')], max_length=200)),
                ('producer', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('avaible', models.CharField(choices=[('Not Avaible', 'Not Avaible'), ('Avaible', 'Avaible')], max_length=15)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
