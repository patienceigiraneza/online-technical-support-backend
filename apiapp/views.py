from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.


# Patience Codes
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
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



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def fn_supporter(request):
    if request.method == 'GET':
        def_support = Supporter.objects.get(user = request.user.id)
        fetch_data = Conversation.objects.filter(supporter=def_support)
        data = ConversationSerializer(fetch_data, many= True)
        return Response(data.data)

    elif request.method == 'POST':
        def_data = SupporterSerializer(data = request.data)
        if def_data.is_valid():
            def_data.save()
            return Response(def_data.data, status=status.HTTP_201_CREATED)
        return Response(def_data.errors, status=status.HTTP_400_BAD_REQUEST)


# Michealla codes
class ViewAllMesseges(APIView):
    def get(self, request):
        message = Message.objects.all()
        serialisers_data = MessageSerializer(message, many=True)
        return Response(serialisers_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialisers_data = MessageSerializer(data=request.data)
        if serialisers_data.is_valid():
            serialisers_data.save()
            return Response(serialisers_data.data, status=status.HTTP_200_OK)
        return Response(serialisers_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewOneMessage(APIView):
    def get(self, request, id):
        message = Message.objects.get(id=id)
        serialisers_data = MessageSerializer(message)
        return Response(serialisers_data.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        message = Message.objects.get(id=id)
        serialisers_data = MessageSerializer(message, data=request.data)
        if serialisers_data.is_valid():
            serialisers_data.save()
            return Response(serialisers_data.data, status=status.HTTP_201_CREATED)
        return Response(serialisers_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        message = Message.objects.get(id=id)
        message.delete()
        return Response({"status":"deleted"}, status=status.HTTP_400_BAD_REQUEST)



# Arlene codes

@api_view(['GET', 'POST'])
def fn_subcategory(request):
    if request.method == 'GET':
        subcategory= SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = SubCategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def fn_view_one_subcategory(request, id):
    try:
        subcategories = SubCategory.objects.get(pk=id)
    except SubCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubCategorySerializer(subcategories)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubCategorySerializer(subcategories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        subcategories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





