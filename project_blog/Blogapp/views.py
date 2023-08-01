from django.shortcuts import render
from .serializers import Blogserial
from .models import BlogInfo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getalldata(request):
    if request.method=='GET':
        blogdata=BlogInfo.objects.all()
        serial=Blogserial(blogdata,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT'])    
def updatedata(request,id):
    try:
        blogid=BlogInfo.objects.get(id=id)
    except BlogInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        Blog=Blogserial(blogid)
        return Response(Blog.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        bloguser=Blogserial(data=request.data,instance=blogid)
        if bloguser.is_valid():
            bloguser.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getid(request,id):
    try:
        id=BlogInfo.objects.get(id=id)
    except BlogInfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serial=Blogserial(id)
    return Response(serial.data,status=status.HTTP_200_OK)


@api_view(['GET','DELETE'])
def deleteid(request,id):
    try:
        id=BlogInfo.objects.get(id=id)
    except BlogInfo.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        serial=Blogserial(id)
        return Response(serial.data,status=status.HTTP_200_OK)
    did=BlogInfo.delete(id)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def insertdata(request):
    if request.method=='POST':
        insert=Blogserial(data=request.data)
        if insert.is_valid():
            insert.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
