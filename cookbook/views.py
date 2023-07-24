from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Recipe might be the wrong argument:
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        # Add Like filter

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                # "likes": likes,
            }
        )


class AddRecipe(View):
    template_name = 'add_recipe.html'
