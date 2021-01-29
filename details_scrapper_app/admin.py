from django.contrib import admin
from .models import Record

# TO MAKE THE `RECORD` AVAILABLE IN ADMIN DASHBOARD
admin.site.register(Record)

# Register your models here.
