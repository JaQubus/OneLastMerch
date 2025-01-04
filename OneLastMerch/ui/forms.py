from django import forms

class ContactForm(forms.Form):
    sender = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        min_length=3,
        max_length=100,
        label="Your email"
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Send your feedback', 'rows': 20, 'cols': 40}),
        min_length=3,
        max_length=5000
    )
