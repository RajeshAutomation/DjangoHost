from django.shortcuts import render
from CBVAPI.models import Studentdbs
from CBVAPI.serializers import Studentserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

# Create your views here.
class studentlist(APIView):
    def get(self,request):
        students = Studentdbs.objects.all()
        serializer = Studentserializer(students,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = Studentserializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

class studendetails(APIView):
    def get_object(self,pk):
        try:
         return Studentdbs.objects.get(pk=pk)
        except:
            return Http404
        
    
    def get(self,request,pk):
        student = self.get_object(pk)
        serializer = Studentserializer(student)
        return Response(serializer.data)
    
    def put(self,request,pk):
        student = self.get_object(pk)
        serializer = Studentserializer(student,data=request.data)
        if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
