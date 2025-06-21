from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    """
    serializer for post
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    image = serializers.ImageField(required=False, allow_null=True)

    def validate_image(self, value):
        """
        validator for image size
        """
        if not value:
            return value

        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image is too large (2MB)')

        if value.image.width > 4096:
            raise serializers.ValidationError('Image width too large')

        if value.image.height > 4096:
            raise serializers.ValidationError('Image height too large')

        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title',
            'movie_title', 'content',
            'image', 'movie_spoilers', 'is_owner',
            'movie_positives', 'movie_negatives',
            'like_id', 'likes_count', 'comments_count'
        ]
