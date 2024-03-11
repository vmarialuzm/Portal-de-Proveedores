from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet, basename='users'),
router.register(r'proveedores', views.ProveedoresViewSet, basename='proveedores')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginApiView.as_view(), name='login'),
]