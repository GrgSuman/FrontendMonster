from django.contrib import admin
from .models import TemplateCategory,Template


class TemplateCategoryAdmin(admin.ModelAdmin):
    model = TemplateCategory
    list_display = ['id','name']


class TemplateAdmin(admin.ModelAdmin):
    model = Template
    list_display = ['id','title','category','likes','createdAt','author',"postStatus"]


admin.site.register(TemplateCategory,TemplateCategoryAdmin)
admin.site.register(Template,TemplateAdmin)
