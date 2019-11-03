from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from ..models import Stream


@login_required
def view(request):
    user = request.user

    return render(request, 'profile.html', {'user': user})

@login_required
@require_POST
def generate_stream_key_view(request):
    user = request.user

    if hasattr(user, 'stream'):
        stream = user.stream
        stream.regenerate_keys()
    else:
        stream = Stream.objects.create(user=user)

    stream.save()

    return redirect('profile')
