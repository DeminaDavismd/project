from django.contrib import admin
from.models import Departmentss,Doctor,appointmet,contact
# Register your models here.
admin.site.register(Departmentss)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','email','doc_name','booked_date')
admin.site.register(appointmet,BookingAdmin)


class contactAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','Type_query')
admin.site.register(contact,contactAdmin)