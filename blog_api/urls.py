# this is the url file for the blog_api application 
from django.contrib import admin
from django.urls import path, include

from blog_api.views import PostDetails, PostList
app_name = 'blop_api'
urlpatterns = [
    # we will be making endpoints to get the post details 
    # endpoint to show a single item 
    path('<int:pk>/', PostDetails.as_view(), name='detailcreate'),
    # endpoint to show all the list items 
    path('', PostList.as_view(), name='listcreate'),
]
