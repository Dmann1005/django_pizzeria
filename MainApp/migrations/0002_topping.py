# Generated by Django 3.0.5 on 2022-12-10 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.TextField()),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Pizza')),
            ],
        ),
    ]
