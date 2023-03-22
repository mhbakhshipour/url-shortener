from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from client.models import User
from client.serializers import UserSerializer, UserPasswordSerializer
from client.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    Only for staff user to manage other users 
    """
    queryset = User.objects.all().order_by("-id")
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

    @action(detail=False, methods=["GET"], permission_classes=[permissions.IsAuthenticated])
    def current_user(self, request):
        """
        For only get detail request user 
        """
        serializer = UserSerializer(request.user, context={
                                    "request": request}).data
        return Response(serializer)

    @swagger_auto_schema(request_body=UserPasswordSerializer, responses={200: "ok", 400: "password is required and must be greater than 8 character"})
    @action(detail=True, methods=["POST"], permission_classes=[permissions.IsAdminUser, IsOwnerOrReadOnly])
    def set_password(self, request, pk):
        """
        For only staff user and request user to change password 
        """
        obj = self.get_object()

        raw_password = request.data.get("password", None)

        if not raw_password or len(raw_password) < 8:
            return Response({"message": "password is required and must be greater than 8 character"}, 400)

        obj.password = make_password(raw_password)
        obj.save(update_fields=["password"])

        return Response({"message": "ok"})
