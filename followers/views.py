from rest_framework import generics, permissions
from my_api.permissions import IsOwnerOrReadOnly
from followers.models import Follower
from followers.serializer import FollowSerializer

# Create your views here.

class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowSerializer
    queryset = Follower.objects.all()


