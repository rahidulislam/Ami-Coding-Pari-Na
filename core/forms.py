from django import forms

class KhojForm(forms.Form):
    input_value = forms.CharField()
    search_value = forms.IntegerField()