# Generated by Django 3.1 on 2020-08-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.TextField(max_length=100)),
                ('emp_id', models.IntegerField()),
                ('emp_sal', models.IntegerField()),
            ],
        ),
    ]