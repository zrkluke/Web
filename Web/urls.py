from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from application import views
from home.views import hello_world, index
from . import settings

urlpatterns = [
    path('hello/', hello_world),
    path('', index, name='index'),
    path('ticket', views.ticket, name='ticket'),
    path('application', views.createApplication, name='application'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
