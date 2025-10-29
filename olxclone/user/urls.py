from django.urls import path
from .views import *


urlpatterns = [
    path('register/', adduser,name='register'),
    path('login/', loginpage,name='login'),
    path('logout/',logoutpage,name='logout'),
    path('profile/',profilepage,name='profile'),
    path('editprofile/<int:eid>',editprofile,name='editprofile'),
    path('addpost',addpost,name='addpost'),
    path('mypost',mypost,name='mypost'),
    path('postpage/<name>',post_page,name='postpage'),
    path('managepost',manage_post,name='managepost'),
    path('editpost/<int:postid>',editpost,name='edit_post'),
    path('deletepost/<int:postid>',deletepost,name='delete_post'),
    path('post_details/<int:postid>',postdetails,name='post_details'),
    path('allpost',allpost,name='allpost'),
    path('addinterestt/<int:postid>/',addinterest,name='addinterest'),
    path('notifications',notifications,name='notifications'),

]

