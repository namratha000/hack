# Generated by Django 3.0.11 on 2020-12-14 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=40)),
                ('link', models.URLField(default='www.jssstuniv.in', max_length=100)),
                ('package', models.CharField(max_length=20)),
                ('last_date_apply', models.DateField()),
                ('location', models.CharField(max_length=15)),
                ('no_of_vacancies', models.IntegerField(default=1)),
                ('type_of_branch', models.CharField(max_length=10)),
                ('no_of_applications', models.IntegerField(default=0)),
                ('al_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Alumni')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Company')),
            ],
            options={
                'unique_together': {('job_id', 'company_id')},
            },
        ),
        migrations.CreateModel(
            name='Applied_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_applied', models.DateField(auto_now=True)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.Vacancies')),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=15)),
                ('Type', models.CharField(max_length=15)),
                ('Date_of_event', models.DateTimeField()),
                ('contact_no', models.CharField(max_length=12)),
                ('std_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Student')),
            ],
        ),
    ]
