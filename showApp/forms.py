from django import forms
from .models import ShowModel
 
# creating a form
class ShowForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ShowModel
 
        # specify fields to be used
        fields = [
            "name",
        ]