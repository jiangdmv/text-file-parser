from django.urls import path, include
from .views import FileViewSet, TimeEventView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'test-files', FileViewSet, basename='upload')

urlpatterns = [
    path('app/', include(router.urls)),
    path('', TimeEventView.as_view(), name='app')
]



