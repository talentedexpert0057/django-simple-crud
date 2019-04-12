# Generated by Django 2.2 on 2019-04-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lswebapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=16)),
                ('date_added', models.DateField()),
            ],
        ),
    ]