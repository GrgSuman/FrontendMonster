from django.shortcuts import render
from django.views import View
from .models import Template,TemplateCategory
from blog.utils import getAllCategories

class TemplateCategoryView(View):
    def get(self,request,blogsCategory):
        # course_category = TemplateCategory.objects.filter(slug=blogsCategory)
        # if related_name not defined in model then course_category[0].course_set.all()
        # courses = course_category[0].course_collection.all()
        # courses = Template.objects.filter(category=course_category[0].id).filter(postStatus=True)
        context={
            'categories':getAllCategories(),
            # 'myCategory':course_category[0],
            # 'courses':courses
        }
        return render(request,"ui_templates/all_template_categories.html",context)