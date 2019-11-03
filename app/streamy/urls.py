from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from .views import home, internal, profile, stream


def nop(*args, **kwargs):
    return HttpResponseServerError()


urlpatterns = [
    path('', home.view, name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile.view, name='profile'),
    path('profile/generate-key', profile.generate_stream_key_view, name='generate-stream-key'),
    path('stream/<name>/', stream.view, name='stream'),
    path('live/<name>.flv', nop, name='flv-url'),
    path('thumb/<name>.png', nop, name='thumbnail-url'),

    # for nginx-rtmp-module callbacks
    path('internal/on_publish', internal.on_publish, name='start-stream'),
    path('internal/on_update', internal.on_update, name='update-stream'),
    path('internal/on_publish_done', internal.on_publish_done, name='stop-stream'),
]
