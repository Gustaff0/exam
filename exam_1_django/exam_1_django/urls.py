"""exam_1_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp.views import hotel_list, hotel_create_view, hotel_edit_view, hotel_delete_view, reg_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hotel_list, name='home'),
    path('create_reg/', hotel_create_view, name='create'),
    path('hotel_reg/<int:pk>/edit/', hotel_edit_view, name='edit'),
    path('hotel_reg/<int:pk>/delete', hotel_delete_view, name='delete')
]
