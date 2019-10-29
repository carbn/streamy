from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import get_object_or_404, render

from ..models import Stream


def view(request, name):
    stream = get_object_or_404(Stream, name=name)

    return render(request, 'stream/view.html', {'stream': stream})
