"""
Provides a form for views at view.py
"""
from ckeditor.fields import RichTextFormField
from django import forms
from django.forms import ModelForm
from .models import Post


class blog_form(ModelForm):
    """
    A form for collecting user information
    """

    class Meta:
        model = Post
        fields = ["title", "content", "status"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Title'}),
            "content": RichTextFormField(config_name="default"),
        }
