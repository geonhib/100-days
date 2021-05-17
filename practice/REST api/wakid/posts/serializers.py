from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    poster_id = serializers.ReadOnlyField(source='poster.id')
    poster = serializers.ReadOnlyField(source='poster.username')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        # exlcude =

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

    def __str__(self):
        """Unicode representation of PostSerializer."""
        pass


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id']

    def __str__(self):
        """Unicode representation of VoteSerializer."""
        pass
