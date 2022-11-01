from django.shortcuts import render
from django.views import View
from .models import Template,TemplateCategory
from blog.utils import getAllCategories

class TemplateCategoryView(View):
    def get(self,request,templateCategory):
        template_category = TemplateCategory.objects.filter(slug=templateCategory)
        # if related_name not defined in model then template_category[0].course_set.all()
        # templates = template_category[0].template_collection.all()
        templates = Template.objects.filter(category=template_category[0].id).filter(postStatus=True)
        context={
            'categories':getAllCategories(),
            'myCategory':template_category[0],
            'templates':templates
        }
        return render(request,"ui_templates/all_template_categories.html",context)

def templateDetail(request,templateDetail):
    blog = Template.objects.get(slug=templateDetail)
    context={
        "blog":blog,
        'categories':getAllCategories()
    }
    return render(request,"ui_templates/templateDetail.html",context)