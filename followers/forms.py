from django import forms



class UserFollowsForm(forms.Form):

    
        

    username_follow = forms.CharField(label='', max_length=60, widget=forms.TextInput(attrs={'size': '60'}))


