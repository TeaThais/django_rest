import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Kitties


# class KittiesModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class KittiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitties
        fields = '__all__'



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
