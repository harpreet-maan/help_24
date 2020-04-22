from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Users
from .models import Trending,FindBusiness,UserRegister,Business_detail,Business_List,category
# Register your models here.


admin.site.register(Trending)
admin.site.register(FindBusiness)
admin.site.register(Business_detail)
admin.site.register(UserRegister)  
admin.site.register(Business_List)
admin.site.register(category)
