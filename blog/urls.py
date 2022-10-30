from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(),name="index"),
    path('category/<slug:blogsCategory>',views.BlogCategoryView.as_view(),name='blogCategory'),
    path("<slug:blogDetail>", views.blogDetail,name="blogDetail"),
]
