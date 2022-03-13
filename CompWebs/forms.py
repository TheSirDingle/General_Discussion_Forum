from django import forms
from .models import GamingPost
from django.utils.html import strip_tags

class PostCreationForm(forms.ModelForm):

    class Meta:
        model = GamingPost
        fields= ['Post_Content']
        exclude = ['author', 'Post_Topic', 'Pdate_Created']



