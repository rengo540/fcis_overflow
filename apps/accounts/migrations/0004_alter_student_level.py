# Generated by Django 4.2.4 on 2023-08-21 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.level'),
        ),
    ]
