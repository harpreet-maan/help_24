

from django.contrib import admin
from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# from .views import ActivateAccount

urlpatterns = [

    path('', views.index, name='index'),
    
    path('index', views.index,name='index'),
    
    path('list', login_required(views.list),name="list"),
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
    path('activate/<uidb64>/<token>/', views.activateAccount, name='activate'),
    path('filtering',views.filtering,name='filtering'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('donor',views.donor,name='donor'),
    path('donorlist',views.donorlist,name='donorlist'),
    path('messagedonor',views.messagedonor,name='messagedonor'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name = 'forgotpassword.html'), name='reset_password'),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(template_name = 'forgotpasswordsent.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'resetpassword.html'), name='password_reset_confirm'),
    path('password-reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('thanks',views.thanks,name='thanks'),



    path("update-profile",login_required(views.UpdateProfile.as_view()),name = "update-profile")

]
