from django import forms
from django.forms import widgets
from webapp.models import *


# class TrackerForm(forms.Form):
#     summary = forms.CharField(max_length=100, required=True, label='Summary')
#     description = forms.CharField(max_length=25000, required=False, label='Description', widget=widgets.Textarea)
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Status', empty_label=None)
#     type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Type', empty_label=None)

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


