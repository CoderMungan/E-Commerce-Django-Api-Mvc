from django import forms

from .models import *


class UpdateProfile(forms.ModelForm):

    class Meta:

        model = ProfileModel
        fields = "__all__"