# Generated by Django 4.2.7 on 2023-11-27 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('role', models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor')], default='student', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
                ('categories', models.ManyToManyField(related_name='categories', to='courses.category')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='courses.user')),
            ],
        ),
    ]
