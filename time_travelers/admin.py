from django.contrib import admin
from .models import TimeTraveler, Skill
# Register your models here.

class AdminTimeTraveler(admin.ModelAdmin):
    list_display=[
        'name',
        'last_name',
        'phone',
        'email',
        'skill',
    ]
    
class AdminSkill(admin.ModelAdmin):
    list_display=[
        'skill'
    ]  
    
admin.site.register(TimeTraveler, AdminTimeTraveler)
admin.site.register(Skill, AdminSkill)
    