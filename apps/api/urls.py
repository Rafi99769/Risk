from rest_framework.routers import DefaultRouter

from apps.risk import apis


router = DefaultRouter()

router.register('risk_type', apis.RiskTypeViewSet, 'risk_type')
router.register('risk_field', apis.RiskFieldViewSet, 'risk_field')

urlpatterns = router.urls
