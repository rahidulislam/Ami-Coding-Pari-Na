# Generated by Django 3.2.7 on 2021-09-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='khojthesearch',
            name='input_value',
        ),
        migrations.AddField(
            model_name='khojthesearch',
            name='input_value',
            field=models.ManyToManyField(to='core.InputValues'),
        ),
    ]
