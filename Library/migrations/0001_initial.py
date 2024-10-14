# Generated by Django 5.1 on 2024-09-25 05:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('published_year', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('menid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('menname', models.TextField(max_length=225)),
                ('menroomno', models.CharField(default='sk2', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('student_phone', models.CharField(max_length=12)),
                ('student_email', models.EmailField(max_length=30)),
                ('stud_status', models.CharField(default='Active', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('borrow_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('borrow_date', models.DateField(max_length=20)),
                ('return_date', models.DateField(max_length=20)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.book')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Library.student')),
            ],
        ),
    ]