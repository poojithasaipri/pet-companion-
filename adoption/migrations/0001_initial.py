# Generated by Django 5.2.4 on 2025-07-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                
                ('description', models.TextField()),
                ('is_adopted', models.BooleanField(default=False)),
            ],
        ),
    ]
