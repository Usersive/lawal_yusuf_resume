from django import forms


class EmailForm(forms.Form):
    sender_name = forms.CharField(max_length=100)
    sender_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)