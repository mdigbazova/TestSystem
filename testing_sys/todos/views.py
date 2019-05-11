from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.


class TodosList(generics.ListCreateAPIView):
    """I use ListCreateAPIView to create a read-only endpoint that lists all available Todo instances"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """I use RetrieveUpdateDestroyAPIView for a detail view of individual todo which supports CRUD-like functionality."""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



