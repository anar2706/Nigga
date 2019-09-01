from django import  forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

        widgets  = {

            'content':forms.TextInput(attrs={'class':'form-control'})



        }