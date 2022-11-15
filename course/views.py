from django.shortcuts import render
from django.views import View
from .models import CourseCategory,Course
from blog.utils import getAllCategories

class CourseCategoryView(View):
    def get(self,request,blogsCategory):
        course_category = CourseCategory.objects.filter(slug=blogsCategory)
        # if related_name not defined in model then course_category[0].course_set.all()
        # courses = course_category[0].course_collection.all()
        courses = Course.objects.filter(category=course_category[0].id).filter(postStatus=True)
        context={
            'categories':getAllCategories(),
            'myCategory':course_category[0],
            'courses':courses
        }
        return render(request,"courses/learn_frontend.html",context)

def courseDetail(request,courseDetail):
    course = Course.objects.get(slug=courseDetail)
    context={
        "course":course,
        'categories':getAllCategories()
    }
    return render(request,"courses/courseDetail.html",context)