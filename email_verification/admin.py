from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'verification_code', 'is_verified')
    search_fields = ('email',)
    list_filter = ('is_verified',)
