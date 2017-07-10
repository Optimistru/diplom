from django.contrib import admin
from .models import *


class UsersTeam(admin.StackedInline):
    model = TeamMember
    fk_name = 'team'
    extra = 0

class UsersAdmin(admin.ModelAdmin):
    inlines = [UsersTeam]

admin.site.register(User, UsersAdmin)