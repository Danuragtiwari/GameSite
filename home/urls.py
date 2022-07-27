# from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
     path(r'^', index,name='index'),
    path(r'^signup/',signup, name='signup'),
   path(r'^login/',login,name='login'),
   path(r'^logout/', logout,name='logout'),
]
