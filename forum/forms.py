from django import forms


class SendComment(forms.Form):
    text = forms.CharField(required=True, max_length=1000, label=None)


class CreateTopic(forms.Form):
    tittle = forms.CharField(required=True, max_length=1000)
    text = forms.CharField(required=True, max_length=10000)

