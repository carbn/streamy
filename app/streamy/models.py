from datetime import timedelta
import functools

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


KEY_LENGTH = 20
key_generator = functools.partial(get_random_string, KEY_LENGTH)

NAME_LENGTH = 8
name_generator = functools.partial(get_random_string, NAME_LENGTH)


class Stream(models.Model):
    class PrivacyMode(models.TextChoices):
        PUBLIC = 'public', _('Public'),
        UNLISTED = 'unlisted', _('Unlisted'),
        LINK = 'link', _('Link'),

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=KEY_LENGTH, default=key_generator, unique=True)
    name = models.CharField(max_length=NAME_LENGTH, default=name_generator, unique=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    privacy = models.CharField(max_length=12, choices=PrivacyMode.choices, default=PrivacyMode.PUBLIC)
    updated_at = models.DateTimeField(null=True, blank=True)

    @property
    def watch_url(self):
        opts = {
            Stream.PrivacyMode.PUBLIC: reverse('stream', args=(self.user.username,)),
            Stream.PrivacyMode.UNLISTED: reverse('stream', args=(self.user.username,)),
            Stream.PrivacyMode.LINK: reverse('stream-link', args=(self.name,)),
        }

        return opts[self.privacy]

    @property
    def flv_url(self):
        return reverse('flv-url', args=(self.name,))

    @property
    def thumbnail_url(self):
        return reverse('thumbnail-url', args=(self.name,))

    @property
    def is_live(self):
        return self.updated_at and self.updated_at + timedelta(seconds=25) > timezone.now()

    def regenerate_keys(self):
        self.key = key_generator()
        self.name = name_generator()

    def __str__(self):
        return self.user.username


class StreamMeta(models.Model):
    stream = models.OneToOneField(Stream, on_delete=models.CASCADE)

    audio = JSONField()
    video = JSONField()

    def __str__(self):
        return str(self.stream)
