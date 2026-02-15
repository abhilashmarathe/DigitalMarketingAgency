from django.contrib import admin

# Register your models here.
from .models import Service
from .models import Testimonial
from .models import Lead

admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Lead)
