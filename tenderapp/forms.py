from django import forms
from .models import PricingClientInfo


class PricingClientForm(forms.ModelForm):
    class Meta:
        model = PricingClientInfo
        fields = "__all__"
