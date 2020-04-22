

from django.contrib import admin
from django.urls import path, include

from . import views
from .views import ActivateAccount

urlpatterns = [

    path('', views.index, name='index'),
    
    path('index', views.index,name='index'),
    
    path('list', views.list,name="list"),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog-single', views.blogsingle, name='blog-single'),
    path('contact', views.contact, name='contact'),
    path('listings', views.listings, name='listings'),
    path('listings/<int:pk>',views.detail,name="detail"),
    path('category/<int:id>',views.categoryList,name = "category"),
    path('listingssingle', views.listingssingle, name='listingssingle'),
    # path('listingssingle/<int:pk>/',views.detail,name="detail"),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout',views.logout,name='logout'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),

]
