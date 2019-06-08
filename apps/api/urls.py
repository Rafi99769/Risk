from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.risk import apis


router = DefaultRouter()

router.register('risk_type', apis.RiskTypeViewSet, 'risk_type')
# router.register('risk_field', apis.RiskFieldViewSet, 'risk_field')
# router.register('enum_choice', apis.EnumChoiceViewSet, 'enum_choice')

urlpatterns = [
    path('single_risk_type/', apis.SingleRiskType.as_view()),
    path('risk_field/', apis.RiskFieldView.as_view()),
    path('', include(router.urls))
]
