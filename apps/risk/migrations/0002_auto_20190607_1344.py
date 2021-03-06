# Generated by Django 2.2.1 on 2019-06-07 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enumchoice',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='risk.RiskField'),
        ),
        migrations.AlterField(
            model_name='riskfield',
            name='risk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_fields', to='risk.RiskType'),
        ),
        migrations.AlterField(
            model_name='risktype',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='enumchoice',
            unique_together={('name', 'field')},
        ),
        migrations.AlterUniqueTogether(
            name='riskfield',
            unique_together={('name', 'risk')},
        ),
    ]
