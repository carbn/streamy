from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from ..models import Stream


@require_POST
@csrf_exempt
def start_stream(request):
    stream = get_object_or_404(Stream, key=request.POST['name'])

    if not stream.user.is_active:
        return HttpResponseForbidden("Inactive user")

    if stream.started_at:
        return HttpResponseForbidden("Already streaming")

    stream.start()
    stream.save()

    return redirect(f'/{stream.user.username}')


@require_POST
@csrf_exempt
def stop_stream(request):
    stream = get_object_or_404(Stream, key=request.POST['name'])

    stream.stop()
    stream.save()

    return HttpResponse()
