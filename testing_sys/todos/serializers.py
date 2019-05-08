from rest_framework import serializers
from .models import Todo, LANGUAGE_CHOICES, STYLE_CHOICES, STATE_CHOICES


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'state', 'language', 'code', 'linenos', 'style', 'owner', 'highlighted') #
        read_only_fields = ('highlighted',)


