from django.db import models


class RiskType(models.Model):
    name = models.CharField(max_length=100)


class RiskField(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=(('text', 'text'), ('number', 'number'),
                                                    ('date', 'date'), ('enum', 'enum')))
    risk = models.ForeignKey(RiskType, on_delete=models.CASCADE, related_name='risk_fields')


class EnumChoice(models.Model):
    name = models.CharField(max_length=100)
    field = models.ForeignKey(RiskField, on_delete=models.CASCADE, related_name='choices')
