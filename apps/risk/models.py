from django.db import models


class RiskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RiskField(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=(('text', 'text'), ('number', 'number'),
                                                    ('date', 'date'), ('enum', 'enum')))
    risk = models.ForeignKey(RiskType, on_delete=models.CASCADE, related_name='risk_fields')

    def __str__(self):
        return "%s - %s" % (self.name, self.risk.name)


class EnumChoice(models.Model):
    name = models.CharField(max_length=100)
    field = models.ForeignKey(RiskField, on_delete=models.CASCADE, related_name='choices')
