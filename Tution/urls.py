from rest_framework.routers import DefaultRouter
from django.urls import include,path
from .views import TuitionViewset

router= DefaultRouter()

router.register('',TuitionViewset)

urlpatterns = [
    path('',include(router.urls)),
]
