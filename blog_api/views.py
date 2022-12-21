from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from blog.models import Post
from .serializer import PostSerializer



# here we will be creating our views in order to give the response to the apis
# we are building backend in django 
class PostDetails(APIView):
    # in this we can define the get and the post request using the function as done below for this purpose 
    def get(self, request, pk):

        # the arguments of the url can be access using the kwargs if the arguments are named in the url 
        # hence we can access the primary key using the following code 
        primaryKey = self.kwargs['pk'];
        
        print("The user has made the get request to get the details about the post \n");
        print("The primary key for the post is ", primaryKey);


        # we have to fetch this data from the database and put it in the serialzer for this purpose 
        currentPost = Post.objects.filter(id = primaryKey);
        currentPost = PostSerializer(currentPost, many=True);
        print("The post after serialization is ", currentPost.data);

        # say everything went fine 
        return Response(currentPost.data);




    
# defining the another view for showing the list of the posts that we have made  till now 
class PostList(APIView):
    print("The endpoint to show the list of the created post is successfully hit\n");
    # we have to return all the list of the post 
    # we have to query the database 
    def get(self, request):
        postList = Post.objects.all();
        
        # now we have to use the serializer in order to convert this query into the readable format called 
        # the json format to send to client in proper format so that client can easily read this for this purpose 
        serializedData = PostSerializer(postList, many=True);
        
        # say everything went fine 
        return Response(serializedData.data);
        
     # now we also have to define the post request for creating new post 
    def post(self, request):
        print("The new post that i am going to insert into the database is as follows \n", request.data);
        serializedData = PostSerializer(data=request.data);
        print("The actual post after serialization is as follows \n", serializedData);

        # now we have to save it 
        if serializedData.is_valid() :
            # then we can save this into the database 
            serializedData.save();
        else:
            # this is not valid hence we can raise a error to the client side 
            return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST);
        
        # this means we have successfully saved the new entry in the database
        return Response(serializedData.data, status=status.HTTP_201_CREATED);
