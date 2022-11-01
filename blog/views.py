from django.views import View
from .models import Category,Blog
from django.core.paginator import Paginator
from django.contrib import messages
import re
from django.shortcuts import render,redirect
from .utils import getAllCategories,createUserSubscription
from course.models import CourseCategory

regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class HomePageView(View):
    def get(self,request):
        blogs = Blog.objects.filter(postStatus=True).order_by("-id")[:12]
        # messages.error(request,"Please enter both name and email")
        frontend_course = CourseCategory.objects.get(id=1)
        context = {
            'categories':getAllCategories(),
            'blogs':blogs,
            'frontend_course':frontend_course
        }
        return render(request,"pages/index.html",context)
    
    def post(self,request):
        name = request.POST['name']
        email = request.POST['email']
        
        if(name=='' or email ==''):
            messages.error(request,"Please enter both name and email")
            return redirect('index')
        else:
            if(re.fullmatch(regexEmail, email)):
                created = createUserSubscription(name,email)
                if created==1:
                    messages.success(request,name+" You have successfully subscribed to our quotes")
                else:
                    messages.error(request,name+", You have already subscribed Frontend Monster")
                return redirect('index')
            messages.error(request,"Please enter valid email")
            return redirect('index')
        
class BlogCategoryView(View):
    def get(self,request,blogsCategory):
        cate = Category.objects.filter(slug=blogsCategory)
        blog = []
        myCategory = ""
        if cate.exists():
                blog = Blog.objects.filter(category=cate[0].id).filter(postStatus=True).order_by("-id")
                myCategory = cate[0]
        else:
            return redirect("index")
        paginator = Paginator(blog, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'categories':getAllCategories(),
            'myCategory':myCategory,
            'blogs':page_obj
        }
        return render(request,"pages/blogCategory.html",context)

def blogDetail(request,blogDetail):
    blog = Blog.objects.get(slug=blogDetail)
    context={
        "blog":blog,
        'categories':getAllCategories()
    }
    return render(request,"pages/blogDetail.html",context)