from rest_framework import viewsets
from rest_framework import permissions

from url.models import Url
from url.serializers import UrlSerializer
from url.permissions import IsOwnerOrReadOnly


class UrlViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = UrlSerializer

    def get_queryset(self):
        queryset = Url.objects.all().order_by("-id")
        if self.request.user.is_staff:
            return queryset
        else:
            queryset = queryset.filter(creator=self.request.user)
            return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)

    def get_serializer_context(self):
        return {"request": self.request}
