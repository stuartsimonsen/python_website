from django.contrib import admin

# Register your models here.
from tracker.models import basictracker,userprofile_extended

admin.site.register(basictracker)
admin.site.register(userprofile_extended)