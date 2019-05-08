from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name="todo-list"),
    path('(?P<int:pk>\d+)/$', views.TodoDetail.as_view(), name="todo-detail"),
]

"""Including format_suffix_patterns is an optional choice that provides a simple, DRY way to refer to a specific file format for a URL endpoint. It means our API will be able to handle URls
 such as http://example.com/api/items/4.json 
 rather than just http://example.com/api/items/4.
"""
urlpatterns = format_suffix_patterns(urlpatterns)