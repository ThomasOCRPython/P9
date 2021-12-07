from django import forms
from django.forms import fields


from . import models


class TicketForm(forms.ModelForm):
    
    class Meta:
        model = models.Ticket
        fields = ['title', 'content','image']


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = models.Review
        fields = ['rating','headline','body']
       
