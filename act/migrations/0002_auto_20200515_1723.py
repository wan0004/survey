# Generated by Django 3.0.6 on 2020-05-15 11:53

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('act', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='place_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='If yes, specify the place!'),
        ),
        migrations.AlterField(
            model_name='housing',
            name='water_source',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('pipe', 'Pipe'), ('river', 'River'), ('handpump', 'Handpump'), ('common pond', 'Common Pond'), ('own pond', 'Own Pond'), ('others', 'Others')], max_length=47),
        ),
        migrations.AlterField(
            model_name='person',
            name='education_level',
            field=models.CharField(choices=[('below matric', 'Below Matric'), ('matriculate', 'Matriculate'), ('12 pass', '12 Pass'), ('graduate', 'Graduate'), ('pg', 'PG'), ('ph.d', 'Ph.D'), ('illetrate', 'Illetrate')], max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='occupation_status',
            field=models.CharField(choices=[('student', 'Student'), ('govt. employee', 'Govt. Employee'), ('unemployed', 'Unemployed'), ('self-employed', 'Self-Employed'), ('cultivator', 'Cultivator'), ('pvt. employee', 'Pvt. Employee'), ('minial job', 'Minial Job'), ('others', 'Others'), ('pensioner', 'Pensioner'), ('house wife', 'House wife')], max_length=50),
        ),
    ]