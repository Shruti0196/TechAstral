from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']

admin.site.register(User, UserAdmin)
admin.site.register(admin_reg)
admin.site.register(Review)
admin.site.register(NGODetails)
admin.site.register(EventDetails)
admin.site.register(CrowdFundingDetails)
admin.site.register(ngo_admin_reg)
admin.site.register(Funding)

