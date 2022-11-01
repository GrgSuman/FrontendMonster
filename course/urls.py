from django.urls import path
from . import views

urlpatterns = [
  path("<slug:blogsCategory>",views.CourseCategoryView.as_view(),name="course_category")
]
