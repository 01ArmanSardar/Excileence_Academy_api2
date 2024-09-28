from rest_framework.routers import DefaultRouter
from django.urls import include,path
from . import views
router = DefaultRouter()
router.register('',views.application)

urlpatterns = [
    path('',include(router.urls)),
    path('delete/<int:pk>',views.deleteapplication,name="deleteApplication")
]
