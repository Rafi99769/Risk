from rest_framework import viewsets, views
from rest_framework.response import Response

from apps.risk import models, serializers


class RiskTypeViewSet(viewsets.ModelViewSet):
    queryset = models.RiskType.objects.all().order_by('-id')
    serializer_class = serializers.RiskTypeSerializer


class SingleRiskType(views.APIView):
    http_method_names = ['get']

    @staticmethod
    def get(request):
        risk_id = request.GET.get('risk_id')
        risk = models.RiskType.objects.get(pk=risk_id)
        result = {'risk': risk.name, 'fields': []}
        for rf in risk.risk_fields.all():
            field = {'id': rf.id, 'field': rf.name, 'type': rf.type, 'choices': []}
            if rf.type == 'enum':
                for c in rf.choices.all():
                    field['choices'].append(c.name)
            result['fields'].append(field)
        return Response(result)


class RiskFieldViewSet(viewsets.ModelViewSet):
    queryset = models.RiskField.objects.all()
    serializer_class = serializers.RiskFieldSerializer


class EnumChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.EnumChoice.objects.all()
    serializer_class = serializers.EnumChoiceSerializer
