from django.contrib import admin
from .models import *
from task.models import *



class ProblemsInline(admin.TabularInline):
    model = ProblemModification.archives.through #многие-ко-многим с ProblemModification
    verbose_name = "ProblemModification"

class ArchiveAdmin(admin.ModelAdmin):
    inlines = [ProblemsInline]

admin.site.register(Archive, ArchiveAdmin)

#************************************************************

class ArchiveTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'name')

admin.site.register(ArchiveType, ArchiveTypeAdmin)