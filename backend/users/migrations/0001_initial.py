# Generated by Django 4.1.7 on 2023-08-31 15:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users_pictures')),
                ('training_level', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.training_level')),
            ],
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('arms', models.FloatField(null=True)),
                ('chest', models.FloatField(null=True)),
                ('waist', models.FloatField(null=True)),
                ('hips', models.FloatField(null=True)),
                ('legs', models.FloatField(null=True)),
                ('body_pictures', models.ImageField(blank=True, upload_to='users_pictures')),
                ('date_register', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='users.user')),
            ],
        ),
    ]