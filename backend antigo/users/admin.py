from django.contrib import admin
from .models import User, Measurements, Training_level

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','training_level')
    list_filter = ('training_level',)
    search_fields = ('name','training_level__level')

class MeansurementsAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'imc')



admin.site.register(User, UserAdmin)
admin.site.register(Measurements, MeansurementsAdmin)
admin.site.register(Training_level)
