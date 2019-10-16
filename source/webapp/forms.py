from django import forms
from django.forms import widgets
from webapp.models import *


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['summary', 'description', 'status', 'type']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']


