"""Forms for Comments and Recipes"""

from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """
    Create Comment Form
    """

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        """
        Get comment model, choose fields to display
        """
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Create Recipe Form
    """

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(attrs={'rows': 3})

    class Meta:
        """
        Get recipe model, choose fields to display and add summernote widget
        """
        model = Recipe
        fields = [
            'title',
            'category',
            'description',
            'preparation_time',
            'cook_time',
            'directions',
            'ingredients',
            'image',
        ]
        widgets = {
            'directions': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }
