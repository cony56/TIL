from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 
            'title',
            'description',
            'content',
            'create_date',
            'modify_date',
            ]