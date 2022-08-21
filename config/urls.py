from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from apps.posts.views import PostViewSet
from apps.videos.views import VideosViewSet
from apps.files.views import FileViewSet

schema_view = get_swagger_view(title="Site back API")

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"videos", VideosViewSet, basename="videos")
router.register(r"files", FileViewSet, basename="files")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("swagger/", schema_view),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
