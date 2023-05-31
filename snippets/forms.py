from django import forms
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        models = Snippet
        fields = ('description', 'snip', 'language')
