from django.contrib import admin
from beb import models
admin.site.register(models.MyJSON, admin.ModelAdmin)