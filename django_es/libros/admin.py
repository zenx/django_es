from django.contrib import admin
from .models import Libro, Editorial


class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'url')
    prepopulated_fields = {'slug': ('nombre',)}

admin.site.register(Editorial, EditorialAdmin)


class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'editorial', 'anio', 'portada',  'url')
    list_filter = ('editorial', 'anio')
    search_fields = ('titulo', 'autor')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('-anio', 'id')

admin.site.register(Libro, LibroAdmin)
