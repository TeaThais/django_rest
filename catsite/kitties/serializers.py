from rest_framework import serializers
from .models import Kitties


class KittiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitties
        fields = ('title', 'cat_id')