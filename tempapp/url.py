from django.contrib import admin
from django.urls import path,include
from tempapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('basePage/',basePage,name='basePage'),
    path('childPage/',childPage,name='childPage'),
    
]    