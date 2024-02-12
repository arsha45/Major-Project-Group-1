# Generated by Django 4.2.9 on 2024-02-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_customuser_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('reason', models.TextField()),
                ('postUser', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
