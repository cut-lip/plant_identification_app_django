# Define views to validate and transform incoming data,
# and to prepare the outgoing data.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SerializerAPI1, SerializerAPI2

# Create your views here.
