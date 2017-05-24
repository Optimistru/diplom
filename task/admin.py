from django.contrib import admin
from .models import *

admin.site.register(Tag)

admin.site.register(AttachmentType)

# admin.site.register(Attachment)


class AttachmentsInline(admin.StackedInline):
    model = Attachment
    extra = 0

class ProblemModificationsInline(admin.StackedInline):
    model = ProblemModification
    extra = 0

class TagsInline(admin.StackedInline):
    model = TagProblem
    extra = 0

class ProblemAdmin(admin.ModelAdmin):
    inlines = [AttachmentsInline, ProblemModificationsInline, TagsInline]

admin.site.register(Problem, ProblemAdmin)

class ProblemModificationAdmin(admin.ModelAdmin):
    inlines = [AttachmentsInline, TagsInline]

admin.site.register(ProblemModification, ProblemModificationAdmin)




