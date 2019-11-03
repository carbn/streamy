from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import get_object_or_404, render


def view(request, name):
    stream = None

    try:
        user = User.objects.get(username=name)
    except User.DoesNotExist:
        user = None

    if user:
        stream = user.stream

    return render(request, 'stream.html', {'stream': stream})
