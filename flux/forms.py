from django import forms



from . import models


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    class Meta:
        model = models.Ticket
        fields = ['title', 'content','image']

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    CHOICES = [(0,0),(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        
        model = models.Review
        fields = ['headline','rating','body']
        # CHOICES = [(0,0),(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        # widgets = {"rating": forms.RadioSelect(choices=CHOICES)
        #            }
       
        
        
class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)