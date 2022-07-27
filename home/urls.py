# from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
     path('', index,name='index'),
    path('signup/',signup, name='signup'),
   path('login/',login,name='login'),
   path('logout/', logout,name='logout'),
]
