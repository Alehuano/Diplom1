from django.contrib import admin
from .models import Manager, Task

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name','department',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('date','payer','sender','recipient','description','urgency','invoice','manager')
    list_filter = ('payer','sender','recipient','manager')
# Register your models here.
