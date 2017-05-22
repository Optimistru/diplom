from django.contrib import admin
from .models import *
from task.models import *



class ProblemsInline(admin.StackedInline):
    model = ProblemModification #or Problem?
    extra = 0

class ArchiveAdmin(admin.ModelAdmin):
    inlines = [ProblemsInline]

admin.site.register(Archive, ArchiveAdmin)

#************************************************************

class ArchiveTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'name')

admin.site.register(ArchiveType, ArchiveTypeAdmin)