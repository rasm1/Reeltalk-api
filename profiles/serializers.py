from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    serializer for profile
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'profile_image', 'created_at', 'updated_at',
            'content', 'image', 'is_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count',
        ]
