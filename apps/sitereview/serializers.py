from rest_framework import serializers
from apps.sitereview.models import Page, Website, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # We only want to display the below fields when returning data
        # You can still send any of the hidden fields in payloads
        fields = ['username', 'user_permissions', 'first_name', 'last_name', 'email', 'id']

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        # All fields will be shown
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # All fields will be shown
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comment_set.all()
        return CommentSerializer(comments, many=True, read_only=True).data

    class Meta:
        model = Page
        # All fields will be shown
        fields = '__all__'
