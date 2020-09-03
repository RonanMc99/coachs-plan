from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': "Enter your name"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Enter your best email"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'What say you?'
    }))