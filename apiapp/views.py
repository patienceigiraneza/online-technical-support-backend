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


@api_view(['GET', 'POST'])
def fn_conversation(request):
    if request.method == 'GET':
        def_client = Client.objects.get(user = request.user.id)
        fetch_data = Conversation.objects.filter(client=def_client)
        data = ConversationSerializer(fetch_data, many= True)
        return Response(data.data)
    elif request.method == 'POST':
        def_data = ConversationSerializer(data = request.data)
        if def_data.is_valid():
            def_data.save()
            return Response(def_data.data, status=status.HTTP_201_CREATED)
        return Response(def_data.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def fn_view_conversation(request, id):
    try:
        fetch_data = Conversation.objects.get(pk=id)
    except Conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        def_serializer = ConversationSerializer(fetch_data)
        return Response(def_serializer.data, safe=False)

    elif request.method == 'PUT':
        def_serializer = ConversationSerializer(fetch_data, data=request.data)
        if def_serializer.is_valid():
            def_serializer.save()
            return Response(def_serializer.data, status=status.HTTP_201_CREATED)
        return Response(def_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fetch_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
