from django import forms

from charityfinderapp.models import Charityinformation


class CharityForm(forms.ModelForm):
    class Meta:
        model = Charityinformation
        fields = "__all__"
