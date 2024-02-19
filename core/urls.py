"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('robots.txt', TemplateView.as_view(template_name = "robots.txt", content_type = "text/pali")),
]

urlpatterns += i18n_patterns(
    #apps
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include("apps.base.urls")),
    path('', include("apps.users.urls")),
    path('', include("apps.faq.urls")),
    path("", include("apps.host.urls")),
    path('', include("apps.chats.urls")),
    path('', include("apps.chef_pages.urls")),
    # prefix_default_language=False,
)
    


    


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)