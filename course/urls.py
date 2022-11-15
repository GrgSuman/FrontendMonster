from django.urls import path
from . import views

urlpatterns = [
  path("category/<slug:blogsCategory>",views.CourseCategoryView.as_view(),name="course_category"),
  path("<slug:courseDetail>",views.courseDetail,name="course_detail")
]
