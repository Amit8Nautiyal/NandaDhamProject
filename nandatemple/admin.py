from django.contrib import admin
from nandatemple.models import Registration

# Register your models here.
class RegisteredDeatilsAdmin(admin.ModelAdmin):
    list_display=('frist_name','last_name', 'mother_name','father_name', 'address', 'gender', 'state', 'city', 'pincode', 'total_person', 'email')

admin.site.register(Registration, RegisteredDeatilsAdmin)
