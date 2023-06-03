from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.EmailField(label="Email", required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your email', 'class': 'form-control'}))
    content = forms.CharField(label="Message", required=True, 
        widget=forms.Textarea(attrs={'placeholder': 'Write your message', 'rows': 4, 'class': 'form-control'}))

    class Meta:
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
        }