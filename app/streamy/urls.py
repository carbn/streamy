from django.urls import path

from .views import internal


def fake_view(*args, **kwargs):
    raise Exception("This should never be called!")


urlpatterns = [
    path('internal/start_stream', internal.start_stream, name='start-stream'),
    path('internal/stop_stream', internal.stop_stream, name='stop-stream'),
    path('live/<username>/index.m3u8', fake_view, name='hls-url')
]
