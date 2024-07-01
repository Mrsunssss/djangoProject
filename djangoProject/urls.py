"""
URL configuration for djangoProject project.

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
from django.urls import path,include,reverse
from django.shortcuts import HttpResponse
from book import views
def index(request):
    # print(reverse("movie:movie_detail", kwargs={'movie_id':1}))
    return HttpResponse("Django自学第一个网页")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sun',index),
    path('book',views.book_detail_query_string),
    # 在book_id中指定参数类型有两点好处：
    # 1.在浏览器中：如果book_id输入一个非整型的值，会报错：http://localhost:8000/sun
    # 2.在视图函数中，得到的book_id就是一个整型，否则默认师str类型
    path('book/<int:book_id>',views.book_detail_path,name="book_detail"),

    path('movie/',include("movie.urls")),

    path('',index,name="index"),

    path('book_1',views.book_html,name="book_html")
]
