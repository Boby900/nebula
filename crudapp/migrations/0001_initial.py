# Generated by Django 4.1.2 on 2024-02-18 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('oid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=20)),
                ('publishedDate', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.book')),
            ],
        ),
    ]
