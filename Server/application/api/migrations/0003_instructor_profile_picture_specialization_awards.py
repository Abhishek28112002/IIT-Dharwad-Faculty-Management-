# Generated by Django 4.2.6 on 2023-10-29 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='profile_picture',
            field=models.FileField(default=' ', upload_to='profile_pics/'),
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Specialization', models.CharField(max_length=255)),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=255)),
                ('award_date', models.DateField()),
                ('award_reason', models.CharField(max_length=255)),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.instructor')),
            ],
        ),
    ]
