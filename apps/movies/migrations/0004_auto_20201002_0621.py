# Generated by Django 3.1.2 on 2020-10-02 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20201002_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedetail',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='movies.movie'),
        ),
    ]