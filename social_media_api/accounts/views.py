from urllib import response
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.follow(target_user)
        return response({"detail": f"You are now following {target_user.username}"})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.unfollow(target_user)
        return response({"detail": f"You unfollowed {target_user.username}"})


class FollowingListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following.all()


class FollowersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.followers.all()