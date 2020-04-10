

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('index', views.index,name='index'),
    path('list', views.list,name="list"),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog-single', views.blogsingle, name='blog-single'),
    path('contact', views.contact, name='contact'),
    path('listings', views.listings, name='listings'),
    path('listings-single', views.listingssingle, name='listings-single'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout',views.logout,name='logout')

]
