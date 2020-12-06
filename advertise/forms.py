from django import forms
from .models import AdvertisingInfo


class AdvertisingForm(forms.ModelForm):
    class Meta:
        model = AdvertisingInfo
        fields = ("name", "banner_size", "email", "contact_no",'organization')

