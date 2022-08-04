from django.contrib import admin
from .models import Parametros

class detParametros(admin.ModelAdmin):
    list_display = ('id','gb','mailTo')
    list_display_links = ('mailTo',)
    search_fields = ('gb','mailTo',)
    list_per_page = 10


admin.site.register(Parametros)