
from django.urls import path,include,re_path

from.views import TweetListView,TweetDetailView,TweetCreateView,TweetUpdateView
app_name='tweets'

urlpatterns = [

    path('',TweetListView.as_view(),name='list'),
    path('<int:pk>',TweetDetailView.as_view(),name='detail'),
    path('new',TweetCreateView.as_view(),name='create'),
    path('<int:pk>/edit/',TweetUpdateView.as_view(),name='create'),
   


]
