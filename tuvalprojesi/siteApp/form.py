from django import forms

from .models import *


class UpdateProfile(forms.ModelForm):

    class Meta:

        model = ProfileModel
        fields = ["profileAvatar","profileBio","profileLocation","profileInstagram","profileTwitter","profileFacebook","profileWebPage"]