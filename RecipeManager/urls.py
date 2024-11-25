"""
URL configuration for RecipeManager project.

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
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login_us/', login_us, name='login_us'),
    path('register/', register, name='register'),
    path('show_recepies/', show_recepies, name='show_recepies'),
    path('logout/', logout_us, name='logout'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('edit/<int:rid>/', edit, name='edit'),
    path('delete/<int:rid>/', delete, name='delete'),
    path('contact/', contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)