"""
URL configuration for Secu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api import views as api_views
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    
    #app_api
    path('', api_views.home, name='home' ),
    path('logout/', api_views.exit, name='exit'),
    path('inicio/', api_views.inicio, name='inicio'),
    path('index/', api_views.index, name='index'),
    path('Crear_Alumno/', api_views.create_alumno, name='create_alumnos'),
    path('Crear_Profesor/', api_views.create_profesor, name='create_profesor'),
    path('Crear_Control/', api_views.create_control, name='Crear_Control'),

    #app_usuarios
    path('usuarios/', usuarios_views.Usuarios, name='usuarios'),
    path('registro/', usuarios_views.register, name='registro' ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
