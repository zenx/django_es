from django.contrib import admin

from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'lugar', 'precio', 'pais', 'ciudad')
    list_filter = ('activo', 'creado', 'modificado')
