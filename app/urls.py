"""
URL configuration for app project.

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
from django.urls import include, path
from django.conf.urls.static import static
from app.settings import MEDIA_ROOT, MEDIA_URL

from main.urls import urlpatterns as main_urls
from authentication.urls import urlpatterns as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls)),
    path('', include(auth_urls)),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
