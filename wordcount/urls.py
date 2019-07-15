# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.urls import path
from . import views #this directory imports views

urlpatterns = [
    path('', views.homepage, name ='home'),
    # path('eggs', views.eggs),
    path('count', views.count, name ='count'), #자유롭게 url 변경 가능
    path('about', views.about, name ='about')
]
