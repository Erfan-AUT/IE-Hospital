# from django.core.serializers.json import DjangoJSONEncoder

# class MessageEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         print(obj)
#         return super().default(obj)

from rest_framework import serializers
from server.models import Message

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Message
        exclude = ('room', 'id', )
