from django.contrib import admin
from .models import CourseCategory,Course


class CourseCategoryAdmin(admin.ModelAdmin):
    model = CourseCategory
    list_display = ['id','name']


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['id','title','category','likes','createdAt','author',"postStatus"]


admin.site.register(CourseCategory,CourseCategoryAdmin)
admin.site.register(Course,CourseAdmin)
