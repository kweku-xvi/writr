from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_blog_or_404(id):
    try:
        blog = Blog.objects.get(id=id)
        return blog
    except Blog.DoesNotExist:
        return None


def blog_not_found_message():
    return Response(
        {
            'success':False,
            'message':'Blog does not exist'
        }, status=status.HTTP_404_NOT_FOUND
    )
    

@api_view(['POST'])
def create_blog(request):
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success':True,
                    'blog':serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def get_blog_by_id(request, id):
    if request.method == 'GET':
        blog = get_blog_or_404(id=id)
        if not blog:
            return blog_not_found_message()

        serializer = BlogSerializer(blog)

        return Response(
            {
                'success':True,
                'blog':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
def get_all_blogs(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()

        serializer = BlogSerializer(blogs, many=True)

        return Response(
            {
                'success':True,
                'blogs':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['PUT', 'PATCH'])
def update_blog(request, id):
    if request.method == 'PUT' or request.method == 'PATCH':
        blog = get_blog_or_404(id=id)
        if not blog:
            return blog_not_found_message()

        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success':True,
                    'blog':serializer.data
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                'success':False,
                'blog':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
def delete_blog(request, id):
    if request.method == 'DELETE':
        blog = get_blog_or_404(id=id)
        if not blog:
            return blog_not_found_message()

        blog.delete()

        return Response(
            {
                'success':True,
                'message':'Blog successfully deleted'
            }, status=status.HTTP_204_NO_CONTENT
        )