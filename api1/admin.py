from .models import Person, ToDo
from django.contrib import admin

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Person, PersonAdmin)


@admin.register(ToDo)
class ToDOAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created", "updated"]