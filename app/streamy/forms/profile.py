from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from ..models import Stream


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = ['title', 'description', 'privacy']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = 'profile'
        self.helper.add_input(Submit('submit', 'Save settings'))
