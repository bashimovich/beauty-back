from rest_framework import routers
from .views import *
from django.urls import include, path


router = routers.SimpleRouter()
router.register('all-companies', ALLCompanyViewSet)
router.register('top-companies', TOPCompanyViewSet)
router.register('wtv-companies', WTVCompanyViewSet)
router.register('test', OrderViewSet)

urlpatterns = [
    path('order', OrderCreateAPIView.as_view(), name='order'),
]

urlpatterns += router.urls
