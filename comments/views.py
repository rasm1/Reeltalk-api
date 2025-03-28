from rest_framework import generics, permissions
from reeltalk_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer, commentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    List view for comments
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List view for comment detail
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = commentDetailSerializer
    queryset = Comment.objects.all()
