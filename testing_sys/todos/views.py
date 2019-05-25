from rest_framework import generics, permissions, renderers
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Todo
from .permissions import IsOwnerOrReadOnly
from .serializers import TodoSerializer, UserSerializer, TodoCreateSerializer
from .method_serializer_view import MethodSerializerView

# Create your views here.


class TodosList(MethodSerializerView, generics.ListCreateAPIView):
    queryset = Todo.objects.all()#RetrieveUpdateDestroyAPIView supports CRUD-like functionality
    serializer_class = TodoSerializer

    method_serializer_classes = {
        ('GET',): TodoSerializer,
        ('POST'): TodoCreateSerializer
    }

    # only authenticated users to be able to create, update, and delete code snippets.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class TodosDetail(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView): #
    queryset = Todo.objects.all() # to create a read-only endpoint that lists
    #all available todoinstances
    serializer_class = TodoCreateSerializer

    method_serializer_classes = {
        ('GET'): TodoSerializer,
        ('PUT', 'PATCH'): TodoCreateSerializer,
    }

    # only authenticated users to be able to create, update, and delete todos.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    """
    To automatically associate the logged-in user with created todo - by overriding 
    .perform_create() method on the todo view - that let's modify how an instance is saved.
    """
    # def perform_create(self, serializer):
    #     import pdb; pdb.set_trace ()
    #     serializer.save(owner=self.request.user)
    # def create(self, validated_data): #
    #     #import pdb; pdb.set_trace()
    #     validated_data['owner'] = self.context['request'].user
    #     return super(TodoSerializer, self).create(validated_data)



"""
To add two new read-only views for a list of all users and a detail view of individual users.
I use the generic class-based RetrieveAPIView for the read-only detail view.
"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
Highlighted Todos Endpoint -  there’s no existing generic view that will work 
so is needed to create my own .get() method.
"""
class TodoDetail(generics.GenericAPIView):#TodoHighlight
    queryset = Todo.objects.all ()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        todo = self.get_object ()
        return Response(todo.highlighted)


"""
To have a single entry point to the API - Root API Endpoint
"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'todos': reverse('todos-list', request=request, format=format)
    })
