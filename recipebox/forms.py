from django import forms
from . import models


class AuthorAdd(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class NewsItemAdd(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=models.Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    prep_time = forms.CharField(max_length=50)


class NewsItemAdd_(forms.ModelForm):
    class Meta:
        model = models.RecipeItem
        fields = ['title', 'author', 'description', 'instructions', 'prep_time']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)