from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManageUsers, Login

router = DefaultRouter()
router.register('user', ManageUsers)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view()),
]
