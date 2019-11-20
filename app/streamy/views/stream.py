from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from ..models import Stream


def user_view(request, name):
    stream = None

    try:
        user = User.objects.get(username=name)
    except User.DoesNotExist:
        user = None

    if user:
        stream = user.stream

    return render(request, 'stream.html', {'stream': stream})


def stream_view(request, name):
    try:
        stream = Stream.objects.get(name=name)
    except Stream.DoesNotExist:
        stream = None

    return render(request, 'stream.html', {'stream': stream})
