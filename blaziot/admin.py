from django.contrib import admin

from .models import Temp

class TempAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['temp_value']}),
        ('Time information', {'fields': ['time_measured'], 'classes': ['collapse']}),
    ]
    list_display = ('temp_value', 'time_measured', 'was_measured_recently')
    
    list_filter = ['time_measured']

admin.site.register(Temp, TempAdmin)




