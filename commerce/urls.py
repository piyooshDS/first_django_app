"""commerce URL Configuration

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
from django.views.generic import TemplateView
from business import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name="login.html"),name="log"),
    url(r'f/',TemplateView.as_view(template_name="frontpage.html"),name="front"),
    url(r'get/',views.valid,name="valid"),
    url(r'check/',views.verify,name="verify"),
    url(r'sell/',views.sell,name="sell"),
    url(r'signout/',views.signout,name="sigout"),
    url(r'data/',views.data,name="data"),
    
]
