from django.contrib import admin
from .models import Contact, Project, Skill, Service, Education

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Contact)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Education)