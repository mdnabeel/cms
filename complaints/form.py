from django import forms


class FaultDetailForm(forms.ModelForm):

    class Media:
        js = ('complaints/static/js/div_showhide.js', )
