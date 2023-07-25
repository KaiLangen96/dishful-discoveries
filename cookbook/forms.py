from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Recipe
        fields = [
            'title',
            'category',
            'excerpt',
            'preparation_time',
            'cook_time',
            'content',
            'ingredients',
            'image',
        ]
        widgets = {
            'content': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }
