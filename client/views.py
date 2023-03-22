from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from client.models import User
from client.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-id")
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

    @action(detail=False, methods=["GET"], permission_classes=[permissions.IsAuthenticated])
    def current_user(self, request):
        serializer = UserSerializer(request.user, context={
                                    "request": request}).data
        return Response(serializer)
