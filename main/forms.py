from django import forms

class importForm(forms.Form):
    league_id = forms.Charfield(label='League ID', max_length=10)