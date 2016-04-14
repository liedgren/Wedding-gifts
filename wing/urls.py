from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout), 
    url(r'^decrease/$', views.decrease), 

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)