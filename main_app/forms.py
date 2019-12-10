from django import forms
from django.forms import ModelForm, Textarea
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'class': 'form-control z-depth-1', 'rows': 7,'style':'width:50%'}),
        }    