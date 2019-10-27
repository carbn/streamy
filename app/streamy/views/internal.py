from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from ..models import Stream


@require_POST
@csrf_exempt
def on_publish(request):
    stream = get_object_or_404(Stream, key=request.POST['name'])

    return redirect(f'/{stream.name}')


@require_POST
@csrf_exempt
def on_update(request):
    stream = get_object_or_404(Stream, key=request.POST['name'])

    stream.updated_at = timezone.now()
    stream.save()

    return HttpResponse()


@require_POST
@csrf_exempt
def on_publish_done(request):
    return HttpResponse()


def hls(*args, **kwargs):
    # this view is actually served by nginx-rtmp
    return HttpResponseServerError()
