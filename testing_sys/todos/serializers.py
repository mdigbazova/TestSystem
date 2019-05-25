from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Todo, LANGUAGE_CHOICES, STYLE_CHOICES, STATE_CHOICES


# relationships between entities -> to use hyperlinks
class TodoSerializer(serializers.ModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='todo-detail', format='html')#

    class Meta:
        model = Todo
        fields = ('url', 'id', 'title', 'created_date', 'end_date', 'description', 'state', 'language', 'code', 'linenos', 'style', 'highlight', 'owner') #
        #read_only_fields = ('highlighted',) -> done in admin.py



class TodoCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    """
    The source argument used here controls which attribute is used to populate a field and can 
    point to any attribute on the serialized instance.
    """

    highlight = serializers.HyperlinkedIdentityField(view_name='todo-detail', format='html')#

    class Meta:
        model = Todo
        fields = ('title', 'created_date', 'end_date', 'description', 'state', 'language', 'code', 'linenos', 'style', 'highlight', 'owner') #
        #read_only_fields = ('highlighted',) -> done in admin.py 'id',

    """
    To automatically associate the logged-in user with created todo - by overriding 
    .perform_create() method on the todo view - that let's modify how an instance is saved.
    """
    def create(self, validated_data): #return ExampleModel.objects.create(**validated_data)
        #import pdb; pdb.set_trace()
        #validated_data['state'] = self.data['state']
        validated_data['owner'] = self.context['request'].user
        return super(TodoCreateSerializer, self).create(validated_data)



class UserSerializer(serializers.ModelSerializer):
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todos-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'todos')

