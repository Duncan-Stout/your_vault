from django import forms

class UploadfileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()