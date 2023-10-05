from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    # path('', ..., name='blog'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)