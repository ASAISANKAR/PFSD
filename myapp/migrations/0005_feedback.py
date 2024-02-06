# Generated by Django 5.0 on 2024-02-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_delete_ss'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('Comments', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]
