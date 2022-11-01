from django.urls import path
from . import views

urlpatterns = [
  path("category/<slug:templateCategory>",views.TemplateCategoryView.as_view(),name="template_category"),
  path("<slug:templateDetail>",views.templateDetail,name="template_detail")
]
