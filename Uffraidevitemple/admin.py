from django.contrib import admin
from Uffraidevitemple.models import UfrainRegistration

class UffrainRagistrationAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email', 'dob', 'phone_no', 'hight', 'weight', 'gender')
# Register your models here.
admin.site.register(UfrainRegistration, UffrainRagistrationAdmin)
