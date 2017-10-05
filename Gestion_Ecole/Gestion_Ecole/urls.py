"""Gestion_Ecole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

admin.autodiscover()

app_name = 'Gestion_Ecole'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login, name='login'),
    url(r'^login$', views.login, name='login'),
<<<<<<< HEAD
    url(r'^logout$', views.logout, name='logout'),
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^classe/(?P<classe_id>[0-9]+)$', views.classe, name='classe'),
=======
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^classe/(?P<classe_id>[0-9]+)$', views.classe, name='classe'),
    #url(r'^register$', registerMaitre),
>>>>>>> 09daf3b251842c1af719889730c976368ff1cb79
]
