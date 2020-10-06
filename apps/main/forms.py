from django import forms


class ShortUrlCreateForm(forms.Form):
	original_url = forms.CharField(widget=forms.URLInput(attrs={"class": "form-control"}))
