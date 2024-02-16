# Generated by Django 4.2.7 on 2023-11-18 20:30

from django.db import migrations, models
import payrollapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0009_addone_employee_alter_step1sub3_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOneEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_employee', models.CharField(choices=[('Employee', 'Employee'), ('Contractor', 'Contractor')], max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('hire_date', models.DateField()),
                ('job_title', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('manager', models.CharField(choices=[('emp01', 'Employee 01'), ('emp02', 'Employee 02')], max_length=20)),
                ('annual_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('location', models.CharField(choices=[('State01', 'State 01'), ('State02', 'State 02')], max_length=20)),
                ('resident_of_india', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='addone_employee',
        ),
        migrations.AlterField(
            model_name='step1sub3',
            name='pincode',
            field=models.CharField(default='', max_length=10, validators=[payrollapp.models.validate_pincode]),
        ),
    ]
