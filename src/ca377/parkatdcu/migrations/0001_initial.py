# Generated by Django 4.1.1 on 2022-09-21 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('campus_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Carpark',
            fields=[
                ('carpark_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('spaces', models.IntegerField()),
                ('disabled_spaces', models.IntegerField()),
                ('campus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkatdcu.campus')),
            ],
        ),
    ]
