from django.shortcuts import render
from .serializers import Bookserial
from .models import Bookinfo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def getalldata(request):
    if request.method=='GET':
        bookdata=Bookinfo.objects.all()
        serial=Bookserial(bookdata,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getid(request,id):
    try:
        bookid=Bookinfo.objects.get(id=id)
    except Bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=Bookserial(bookid)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['GET','DELETE'])
def deleteid(request,id):
    try:
        bookid=Bookinfo.objects.get(id=id)
    except Bookinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        userserial=Bookserial(bookid)
        return Response(userserial.data,status=status.HTTP_200_OK)
    Bookinfo.delete(bookid)
    return Response (status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def postdata(request):
    if request.method=='POST':
        bookdata=Bookserial(data=request.data)
        print(bookdata)
        if bookdata.is_valid():
            bookdata.save()
            return Response (status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT'])
def updatedata(request,id):
    try:
        bookid=Bookinfo.objects.get(id=id)
    except Bookinfo.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        userserial=Bookserial(bookid)
        return Response (userserial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        userserial=Bookserial(data=request.data,instance=bookid)
        if userserial.is_valid():
            userserial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response (status=status.HTTP_400_BAD_REQUEST)