import json

from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from ..models import Stream, StreamMeta


@require_POST
@csrf_exempt
def on_publish(request):
    stream = get_object_or_404(Stream, key=request.POST['name'])

    location = f'rtmp://127.0.0.1:1935/live/{stream.name}'
    response = HttpResponse(location, status=302)
    response['Location'] = location

    return response


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


@require_POST
@csrf_exempt
def update_meta(request, name):
    json_data = json.loads(request.body.decode('utf-8'))

    stream = get_object_or_404(Stream, name=name)

    data = {
        'audio': None,
        'video': None,
    }

    for item in json_data['streams']:
        t = item['codec_type']

        if t in data.keys():
            data[t] = item

    meta, created = StreamMeta.objects.update_or_create(stream=stream, defaults=data)

    return HttpResponse()
