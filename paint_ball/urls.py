"""paint_ball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from core.views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet, base_name='player')
router.register(r'teams', TeamViewSet, base_name='team')
router.register(r'guns', GunViewSet, base_name='gun')
router.register(r'maps', MapViewSet, base_name='map')
router.register(r'shots', ShotViewSet, base_name='shot')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^login/', obtain_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token),

]

urlpatterns = router.urls + urlpatterns
