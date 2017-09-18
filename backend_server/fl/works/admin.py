from django.contrib import admin

# Register your models here.

from .models import Work, WorkCategory

admin.site.register(Work)
admin.site.register(WorkCategory)
