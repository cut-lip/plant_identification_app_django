# Define views to validate and transform incoming data,
# and to prepare the outgoing data.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SerializerAPI1, SerializerAPI2

# Define API view classes
class API1View(APIView):
    def get(self, request):
        data = [
            {"name": "Item 1", "value": 10},
            {"name": "Item 2", "value": 20},
        ]
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SerializerAPI1(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class API2View(APIView):
    def get(self, request):
        data = [
            {"name": "Item 1", "value": 10},
            {"name": "Item 2", "value": 20},
        ]
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SerializerAPI2(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)