# Generated by Django 3.0.6 on 2020-05-31 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register', models.BooleanField(default=True)),
                ('guild', models.BooleanField(default=True)),
                ('password', models.CharField(default='4194d1706ed1f408d5e02d672777019f4d5385c766a8c6ca8acba3167d36a7b9', max_length=64)),
            ],
        ),
    ]