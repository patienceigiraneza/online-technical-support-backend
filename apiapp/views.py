from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response

# Create your views here.


def fn_rest_register(request):
    def_data = UserSerializer(data = request.data)
    if def_data.is_valid():
        def_data.save()
        return Response(def_data.data, status=status.HTTP_201_CREATED)
    return Response(def_data.errors, status=status.HTTP_400_BAD_REQUEST)


def fn_home(request):
    pass
