from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Recipe
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Recipe might be the wrong argument:
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.order_by('created_on')
        # Add Like filter

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "comment_form": CommentForm(),
                # "likes": likes,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        # favourite = False
        # if recipe.favourites.filter

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                # "commented": True,
                "comment_form": CommentForm()
                # "favourite": favourite
            },
        )


class AddRecipe(generic.CreateView):
    form_class = RecipeForm()
    template_name = 'add_recipe.html'
    success_url = reverse_lazy('add_recipe')

    def form_valid(self, form):
        form.instance.author = self.request.user
        super(AddRecipe, self).form_valid(form)
        return redirect('add_recipe')
