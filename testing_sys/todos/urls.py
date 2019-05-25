from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from . import views

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view),
    path('todos_list/', views.TodosList.as_view(), name="todos-list"),
    path('todo/<pk>/', views.TodosDetail.as_view(), name="todos-detail"),
    path('todo/<pk>/highlight/', views.TodoDetail.as_view(), name='todo-detail'),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('user/<pk>/', views.UserDetail.as_view (), name="user-detail"),
    path('', views.api_root),
]

"""Including format_suffix_patterns is an optional choice that provides a simple, DRY way to refer to a specific file format for a URL endpoint. It means our API will be able to handle URls
 such as http://example.com/api/items/4.json 
 rather than just http://example.com/api/items/4.
"""
urlpatterns = format_suffix_patterns(urlpatterns)
