from django.db import transaction
from rest_framework import viewsets, views, status
from rest_framework.response import Response

from apps.risk import models, serializers


class RiskTypeViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
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


class RiskFieldView(views.APIView):
    http_method_names = ['put', 'post']

    @staticmethod
    def post(request):
        risk_id = request.data.get('risk_id')
        enum_choices = []

        with transaction.atomic():
            try:
                for field in request.data.get('risk_fields'):
                    risk_field = models.RiskField.objects.create(name=field['name'],
                                                                 type=field['type'],
                                                                 risk_id=risk_id)

                    if field['type'] == 'enum':
                        for choice in field['choices']:
                            enum_choices.append(models.EnumChoice(field_id=risk_field.id, 
                                                                  name=choice))

                models.EnumChoice.objects.bulk_create(enum_choices)
            except Exception as e:
                return Response({'detail': str(e.__cause__).split("Key")[1]},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'Success': 'Post Successful!'})

    @staticmethod
    def put(request):
        pass


class RiskFieldViewSet(viewsets.ModelViewSet):
    queryset = models.RiskField.objects.all()
    serializer_class = serializers.RiskFieldSerializer


class EnumChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.EnumChoice.objects.all()
    serializer_class = serializers.EnumChoiceSerializer
