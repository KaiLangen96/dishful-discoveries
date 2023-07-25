"""Views"""

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


class Home(View):
    """
    This view is used to display the home page
    """
    # template_name = 'index.html'

    def get(self, request):
        return render(request, 'index.html')


class RecipeList(generic.ListView):
    """
    This view is used to display all recipes in the browse recipes page
    """
    model = Recipe
    queryset = Recipe.objects.order_by('-created_on')
    template_name = 'browse_recipes.html'
    paginate_by = 8


class RecipeDetail(View):
    """
    This view is used to display the full recipe details including comments
    It also includes the comment form
    """

    def get(self, request, slug):
        """
        Retrives the recipe and related comments from the database
        """
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "comment_form": CommentForm(),
                "liked": liked,
            },
        )

    def post(self, request, slug):
        """
        This method is called when a POST request is made to the view
        via the comment form.
        """
        recipe = get_object_or_404(Recipe, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

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
                "comment_form": CommentForm(),
                "liked": liked,
            },
        )


class AddRecipe(LoginRequiredMixin, SuccessMessageMixin,
                generic.CreateView):
    """
    This view is used to allow logged in users to create a recipe
    """
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of the recipe.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the recipe title into the success message.
        source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class MyRecipes(LoginRequiredMixin, generic.ListView):
    """
    This view is used to display a list of recipes created by the logged in
    user.
    """
    model = Recipe
    template_name = 'my_recipes.html'
    paginate_by = 8

    def get_queryset(self):
        """
        Override get_queryset to filter by user
        """
        return Recipe.objects.filter(author=self.request.user)


class UpdateRecipe(LoginRequiredMixin, UserPassesTestMixin,
                   SuccessMessageMixin, generic.UpdateView):
    """
    This view is used to allow logged in users to edit their own recipes
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'update_recipe.html'
    success_message = "%(calculated_field)s was updated successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of the recipe.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Prevent another user from updating someone else's recipe
        """
        recipe = self.get_object()
        return recipe.author == self.request.user

    def get_success_message(self, cleaned_data):
        """
        Override the get_success_message() method to add the recipe title
        into the success message.
        source: https://docs.djangoproject.com/en/4.0/ref/contrib/messages/
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin,
                   generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own recipes
    """
    model = Recipe
    template_name = 'delete_recipe.html'
    success_message = "Recipe deleted successfully"
    success_url = reverse_lazy('my_recipes')

    def test_func(self):
        """
        Prevent another user from deleting someone else's recipe
        """
        recipe = self.get_object()
        return recipe.author == self.request.user

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)


class LikeRecipe(LoginRequiredMixin, View):
    """
    This view allows a logged in user to bookmark recipes.
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Checks if user id already exists in the favourites
        field in the Recipe database.
        If they exist then remove them from the database.
        If they don't exist then add them to the database.
        """
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
            messages.success(self.request, 'Recipe removed from likes')
        else:
            recipe.likes.add(request.user)
            messages.success(self.request, 'Recipe added to likes')
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class MyLikes(LoginRequiredMixin, generic.ListView):
    """
    This view allows a logged in user to view their liked recipes.
    """
    model = Recipe
    template_name = 'my_likes.html'
    paginate_by = 8

    def get_queryset(self):
        """
        Override get_queryset to filter by user likes
        """
        return Recipe.objects.filter(likes=self.request.user.id)


class UpdateComment(LoginRequiredMixin, UserPassesTestMixin,
                    SuccessMessageMixin, generic.UpdateView):
    """
    This view is used to allow logged in users to update their own comments
    """
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
    success_message = "Comment updated successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        The signed in user is set as the author of the comment.
        """
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        """
        Prevent another user from updating someone else's recipe
        """
        comment = self.get_object()
        return comment.name == self.request.user.username

    def get_success_url(self):
        """
        Return to recipe detail view when comment updated sucessfully
        """
        recipe = self.object.recipe
        return reverse_lazy('recipe_detail', kwargs={'slug': recipe.slug})


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin,
                    generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own comments
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_message = "Comment deleted successfully"

    def test_func(self):
        """
        Prevent another user from deleting someone else's comment
        """
        comment = self.get_object()
        return comment.name == self.request.user.username

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Return to recipe detail view when comment deleted sucessfully
        """
        recipe = self.object.recipe
        return reverse_lazy('recipe_detail', kwargs={'slug': recipe.slug})
