from django.contrib import admin
from .models import CustomUser, CV, PageView

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_staff')
    search_fields = ('first_name', 'surname', 'email', 'skills')

admin.site.register(CustomUser, CustomUserAdmin)

class CVAdmin(admin.ModelAdmin):
    list_display = ('work_experience', 'education')

admin.site.register(CV, CVAdmin)

class PageViewAdmin(admin.ModelAdmin):
    list_display = ('page', 'user', 'timestamp', 'ip_address', 'location')

admin.site.register(PageView, PageViewAdmin)
