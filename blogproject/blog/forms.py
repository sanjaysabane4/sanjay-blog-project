from django import forms

class EmailSendForm(forms.Form):
    name = forms.CharField(max_length=265)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)