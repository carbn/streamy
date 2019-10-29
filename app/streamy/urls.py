from django.urls import path

from .views import internal, stream


urlpatterns = [
    path('stream/<name>/', stream.view, name='stream'),
    path('internal/on_publish', internal.on_publish, name='start-stream'),
    path('internal/on_update', internal.on_update, name='update-stream'),
    path('internal/on_publish_done', internal.on_publish_done, name='stop-stream'),
    path('hls/<name>/index.m3u8', internal.hls, name='hls-url')
]
