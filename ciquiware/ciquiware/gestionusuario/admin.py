# admin.py en tu aplicación gestionusuario
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Division, Area, Grupo, ART, Firma

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'rut', 'cargo'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'rut', 'cargo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'rut', 'cargo', 'is_staff')
    search_fields = ('username', 'email', 'rut')

class GrupoAdmin(admin.ModelAdmin):
    model = Grupo
    filter_horizontal = ('trabajadores',)

class ARTAdmin(admin.ModelAdmin):
    model = ART
    list_display = ('id', 'grupo', 'fecha', 'cantidad_firmas')

class FirmaAdmin(admin.ModelAdmin):
    model = Firma
    list_display = ('art', 'usuario', 'fecha_firma')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Division)
admin.site.register(Area)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(ART, ARTAdmin)
admin.site.register(Firma, FirmaAdmin)
