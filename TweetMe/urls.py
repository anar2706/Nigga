
from django.contrib import admin
from django.urls import path,include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tweets.urls',namespace='tweets')),
    re_path(r'^accounts/', include('allauth.urls')),
]
