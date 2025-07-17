from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MeView, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
]

urlpatterns += router.urls
