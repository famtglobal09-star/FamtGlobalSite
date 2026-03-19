from django import forms

from website.models import CallbackRequest



class CallbackForm(forms.ModelForm):

    class Meta:
        model = CallbackRequest
        fields = ['name','email','phone','service','message']