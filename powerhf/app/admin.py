from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import *

class UserAccountsAdmin(UserAdmin):
    list_display = ['id','username' ,'first_name' ,'last_name' ,'email' ,'department', 'date_joined', 'last_login','is_staff','is_admin','is_active','is_superuser']
    search_fields = ['id','username','first_name','last_name' ,'email' ,'department']
    readonly_fields = ['date_joined','last_login']

    filter_horizontal = []
    list_filter = []
    fieldsets = []
admin.site.register(Users, UserAccountsAdmin)


admin.site.register(EnergyFuel)

admin.site.register(FuelDrawn)