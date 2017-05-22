from django.contrib import admin
from .models import *

admin.site.register(AttachmentType)

# admin.site.register(Attachment)


class AttachmentsInline(admin.StackedInline):
    model = Attachment
    extra = 0

class ProblemAdmin(admin.ModelAdmin):
    inlines = [AttachmentsInline]

admin.site.register(Problem, ProblemAdmin)

class ProblemModificationAdmin(admin.ModelAdmin):
    inlines = [AttachmentsInline]

admin.site.register(ProblemModification, ProblemModificationAdmin)




