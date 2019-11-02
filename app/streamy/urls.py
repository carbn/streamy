from django.urls import path

from .views import home, internal, stream


urlpatterns = [
    path('', home.view, name='home'),
    path('stream/<name>/', stream.view, name='stream'),
    path('live/<name>.flv', internal.nop, name='flv-url'),
    path('thumb/<name>.png', internal.nop, name='thumbnail-url'),

    # for nginx-rtmp-module callbacks
    path('internal/on_publish', internal.on_publish, name='start-stream'),
    path('internal/on_update', internal.on_update, name='update-stream'),
    path('internal/on_publish_done', internal.on_publish_done, name='stop-stream'),
]
