from datetime import timedelta

from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.utils import timezone

from ..models import Stream


def view(request):
    # todo: should not duplicate this filter in the stream model
    live_streams = Stream.objects.filter(updated_at__gte=timezone.now() - timedelta(minutes=1)).order_by('name')
    live_streams = [s for s in live_streams if s.is_live]

    return render(request, 'home.html', {'streams': live_streams})
