from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def fn_registration(request):
    def_data = UserSerializer(data = request.data)
    if def_data.is_valid():
        def_data.save()
        return Response(def_data.data, status=status.HTTP_201_CREATED)
    return Response(def_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fn_home(request):
    pass

@api_view(['GET'])
def fn_category(request):
    fetch_data = Category.objects.all()
    data = CategorySerializer(fetch_data, many= True)
    return Response(data.data)

