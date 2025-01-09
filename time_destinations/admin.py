from django.contrib import admin
from .models import TimeDestination,Type

# Register your models here.
class AdminTimeDestination(admin.ModelAdmin):
    list_display=[
        'name',
        'type',
    ]

class AdminType(admin.ModelAdmin):
    list_display=[
        'type'
    ]


admin.site.register(TimeDestination, AdminTimeDestination)
admin.site.register(Type, AdminType)