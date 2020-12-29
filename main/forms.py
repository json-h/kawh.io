from django import forms

class league_form(forms.Form):
    league_id = forms.CharField(
        label="League ID", 
        max_length=10,
        widget=forms.TextInput(attrs={'class':'input is-small','placeholder':'League ID'})
        )
    private = forms.BooleanField(
        label="Private", 
        required=False,
        widget=forms.CheckboxInput(attrs={'id':'chk','onClick':'toggleFields()'})
        )
    espn_s2 = forms.CharField(
        label="ESPN_S2", 
        required=False,
        max_length=400,
        widget=forms.TextInput(attrs={'class':'input is-small','placeholder':'ESPN_S2'})
        )
    swid = forms.CharField(
        label="SWID", 
        required=False, 
        max_length=40,
        widget=forms.TextInput(attrs={'class':'input is-small','placeholder':'SWID'})
        )