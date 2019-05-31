from rest_framework import viewsets

from apps.risk import models, serializers


class RiskTypeViewSet(viewsets.ModelViewSet):
    queryset = models.RiskType.objects.all()
    serializer_class = serializers.RiskTypeSerializer


class RiskFieldViewSet(viewsets.ModelViewSet):
    queryset = models.RiskField.objects.all()
    serializer_class = serializers.RiskFieldSerializer
