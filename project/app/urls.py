from django.urls import path, include
from rest_framework import routers

from app import views


router = routers.DefaultRouter()
router.register(r'keys', views.KeyViewSet, 'Key')
router.register(
    r'keys/(?P<key_id>[0-9]+)/translations',
    views.TranslationViewSet,
    'Translation',
)

urlpatterns = [
    path('', include(router.urls)),
]