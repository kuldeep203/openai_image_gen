# imagegen/models.py

# imagegen/forms.py

from django import forms

class ImageForm(forms.Form):
    prompt = forms.CharField(label='Prompt', max_length=255)
