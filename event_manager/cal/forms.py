from .models import Event
from django import forms

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields= '__all__' #["id", "fecha", "dia", "hora_inicio", "hora_fin", "grupo", "profesor" ]