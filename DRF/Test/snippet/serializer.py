from rest_framework import serializers
from .models import Snippet

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title=validated_data.get('title', instance.title)
        instance.code=validated_data.get('code', instance.code)
        instance.linenos=validated_data.get('linenos', instance.linenos)
        instance.save()
        return instance
