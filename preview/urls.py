from django.conf.urls import url
from django.conf.urls.static import static

from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Web import settings
from preview import views

urlpatterns = [
    path('preivew', views.previewApplication),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






