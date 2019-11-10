from datetime import timedelta
import functools

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string


KEY_LENGTH = 20
key_generator = functools.partial(get_random_string, KEY_LENGTH)

NAME_LENGTH = 8
name_generator = functools.partial(get_random_string, NAME_LENGTH)


class Stream(models.Model):
    PRIVACY_CHOICES = (
        ('public', 'Public'),
        ('unlisted', 'Unlisted'),
        #('followers', 'Followers only'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=KEY_LENGTH, default=key_generator, unique=True)
    name = models.CharField(max_length=NAME_LENGTH, default=name_generator, unique=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    privacy = models.CharField(max_length=12, choices=PRIVACY_CHOICES, default='public')
    updated_at = models.DateTimeField(null=True, blank=True)

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
