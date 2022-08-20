from rest_framework import viewsets

from .models import Video
from .serializers import VideoSerializer


class VideosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
