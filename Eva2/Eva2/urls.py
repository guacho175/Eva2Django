"""
URL configuration for Eva2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from regiones import views as vista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.RegionesCatalogo, name='CatalogoRegiones'),
    path('catalogo_comunas/<int:region_id>/', vista.detalle_comunas, name='catalogo_comunas'),
    path('catalogo_comunas_todas/', vista.ComunasCatalogo, name='catalogo_comunas_todas'),
    path('detalle_comuna/<int:comuna_id>/', vista.detalle_comuna, name='detalle_comuna'),
    path('eliminar_comuna/<int:comuna_id>/', vista.eliminar_comuna, name='eliminar_comuna'),



]
