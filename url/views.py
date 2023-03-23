from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

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


class ShortUrlViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, path, format=None):
        try:
            url = Url.objects.get(short_url_id=path)
        except Url.DoesNotExist:
            return Response({"message": "Not found"}, 404)

        res = UrlSerializer(url).data
        return Response(res)
