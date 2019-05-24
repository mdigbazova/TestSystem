from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Todo, LANGUAGE_CHOICES, STYLE_CHOICES, STATE_CHOICES


# relationships between entities -> to use hyperlinks
class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    """
    The source argument used here controls which attribute is used to populate a field and can 
    point to any attribute on the serialized instance.
    """
    highlight = serializers.HyperlinkedIdentityField(view_name='TodoHighlight', format='html')#todo - highlight

    class Meta:
        model = Todo
        fields = ('url', 'id', 'title', 'created_date', 'description', 'state', 'language', 'code', 'linenos', 'style', 'highlight', 'owner') #
        #read_only_fields = ('highlighted',) -> done in admin.py
        #


class UserSerializer(serializers.ModelSerializer):
    #todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'todos')