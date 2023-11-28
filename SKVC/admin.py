from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Service)
admin.site.register(CarouselSlide)
admin.site.register(Project)
admin.site.register(ProjectImage)

admin.site.register(Appointment)