from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(Tag)

admin.site.register(AttachmentType)


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

class CompanyInline(admin.StackedInline):
    model = Company
    verbose_name_plural = 'компании'
    verbose_name = 'Компания'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CompanyInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


