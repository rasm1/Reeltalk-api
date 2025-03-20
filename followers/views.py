from rest_framework import generics, permissions
from reeltalk_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    list view for followers
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    list view for follower detail
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
