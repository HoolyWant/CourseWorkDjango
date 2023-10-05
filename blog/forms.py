from django import forms

from blog.models import Blog
from mail.forms import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('user', 'count',)
