from django.urls import path
# from . import views
from .views import Tweetlistview,Tweetcreateview,TweetUpdateview,TweetDeleteview

urlpatterns = [
    path('',Tweetlistview.as_view(),name='home'),
    path('create/',Tweetcreateview.as_view(),name='tweetcreate'),
    path('tweet/<int:pk>/update',TweetUpdateview.as_view(),name='tweetupdate'),
    path('tweet/<int:pk>/delete',TweetDeleteview.as_view(),name='tweetdelete'),
]
