# Generated by Django 2.0.1 on 2018-06-12 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Author'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='topic',
        ),
        migrations.AddField(
            model_name='book',
            name='topic',
            field=models.ManyToManyField(blank=True, null=True, to='app.Topic'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Author'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Book'),
        ),
        migrations.RemoveField(
            model_name='quote',
            name='tag',
        ),
        migrations.AddField(
            model_name='quote',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='app.Tag'),
        ),
    ]