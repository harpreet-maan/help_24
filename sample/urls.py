from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import view
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = 'Help_24 Administration'                     
admin.site.index_title = 'Help_24 Admin'                 
admin.site.site_title = 'Help_24 Management'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.url')),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
