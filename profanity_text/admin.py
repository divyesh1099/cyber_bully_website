from django.contrib import admin
from .models import Cusslist

# Register your models here.
@admin.register(Cusslist)
class CusslistAdmin(admin.ModelAdmin):
    list_display = ['cussword', 'created', 'edited']
    search_fields = ['cussword']
