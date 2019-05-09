from django.urls import path, include
from rest_framework import routers

from app import views


router = routers.DefaultRouter()

router.register(
    prefix=r'keys', 
    viewset=views.KeyViewSet, 
    base_name='Key'
)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'keys/<int:key_id>/translations/', 
        views.TranslationListView.as_view(),
    ),
    path(
        'keys/<int:key_id>/translations/<str:locale>/', 
        views.TranslrationDetailView.as_view(),
    ),
]