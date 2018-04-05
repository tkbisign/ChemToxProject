# Generated by Django 2.0.2 on 2018-03-07 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20180307_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment_citation_relation',
            name='aeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.experiment'),
        ),
        migrations.AlterField(
            model_name='experiment_citation_relation',
            name='citation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.citation'),
        ),
    ]
