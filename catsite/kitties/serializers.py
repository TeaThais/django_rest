import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Kitties


# class KittiesModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class KittiesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Kitties.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance


# def encode():
#     model = KittiesModel('Sarabi', 'a lioness')
#     model_serialized = KittiesSerializer(model)
#     print(model_serialized.data, type(model_serialized.data), sep='\n')
#     json = JSONRenderer().render(model_serialized.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Sarabi","content":"a lioness"}')
#     data = JSONParser().parse(stream)
#     serializer = KittiesSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
