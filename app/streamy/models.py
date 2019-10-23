import functools

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string


KEY_LENGTH = 20
key_generator = functools.partial(get_random_string, KEY_LENGTH)


class Stream(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=KEY_LENGTH, default=key_generator, unique=True)
    started_at = models.DateTimeField(null=True, blank=True)

    @property
    def live(self):
        return self.started_at is not None

    @property
    def url(self):
        return reverse('hls-url', args=(self.user.username,))

    def start(self):
        self.started_at = timezone.now()

    def stop(self):
        self.started_at = None

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Stream.objects.create(user=instance)
