# relatorios/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfis de Especialidade'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Anula o registro do modelo User padrão e o registra novamente com o ProfileInline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
