from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogList, BlogEdit, BlogCreate, BlogDelete, BlogDetail

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('blog_edit/<int:pk>', BlogEdit.as_view(), name='blog_edit'),
    path('blog_create', BlogCreate.as_view(), name='blog_create'),
    path('blog_delete/<int:pk>', BlogDelete.as_view(), name='blog_delete'),
    path('blog_detail/<int:pk>', BlogDetail.as_view(), name='blog_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
