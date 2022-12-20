from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Post
# Create your views here.
# here we will be creating our views in order to give the response to the apis
# we are building backend in django 
class PostDetails(APIView):
    # in this we can define the get and the post request using the function as done below for this purpose 
    def get(self, request, pk):
        primaryKey = self.kwargs['pk'];
        print("The user has made the get request to get the details about the post \n");
        print("The primary key for the post is ", primaryKey);

        # say everything went fine 
        return Response({"message" : "everything is alright"});
    
# defining the another view for showing the list of the posts that we have made  till now 
class PostList(APIView):
    print("The endpoint to show the list of the created post is successfully hit\n");
    # we have to return all the list of the post 
    # we have to query the database 
    postList = Post.objects.all();

    # now we have to use the serializer in order to convert this query into the readable format called 
    # the json format to send to client in proper format so that client can easily read this for this purpose 
    