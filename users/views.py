from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        return Response({"message": "This is an admin-only view."})

class ModeratorOnlyView(APIView):
    def get(self, request):
        if request.user.role == 'Moderator':
            return Response({"message": "This is a moderator-only view."})
        return Response({"message": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
# Create your views here.
