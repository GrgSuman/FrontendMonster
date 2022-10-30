from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("blog.urls")),
    path("courses",include("course.urls")),
    path("ui",include("ui_templates.urls")),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

admin.site.site_header = "IELTS Frontend Monster Administration"
admin.site.site_title = "IELTS Frontend Monster Admin Portal"
admin.site.index_title = "Welcome to IELTS Frontend Monster"
