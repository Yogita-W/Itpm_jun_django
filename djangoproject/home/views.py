'''from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def home(request):
    return Response({
        'status': 200,
        'message': 'Yes! DjangoRestFramework Working...'
    })
'''
    
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


@api_view(['GET', 'POST'])
def post_list(request):

    # GET request → fetch all posts
    if request.method == 'GET':
        posts = Post.objects.all()#to store object of post model
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # POST request → create new post
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Post Created Successfully',
                'data': serializer.data
            })
        return Response(serializer.errors)
