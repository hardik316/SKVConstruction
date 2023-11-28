from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('contactus', contactus, name='contactus'),
    path('services/', service, name='service'),
    path('service/<int:pk>/', service_detail, name='service_detail'),
    path('appointment/', appointment, name='appointment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)