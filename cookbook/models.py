"""Models"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Model for Category
    """
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Model for Recipe
    """
    title = models.CharField(max_length=70, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    preparation_time = models.CharField(max_length=10, default=0)
    cook_time = models.CharField(max_length=10, default=0)
    excerpt = models.TextField(blank=True)
    ingredients = models.TextField()
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='likes', default=None, blank=True)

    class Meta:
        """
        To display the recipes by created_on in descending order
        """
        ordering = ['-created_on']

    def get_absolute_url(self):
        """
        Get url after user adds/edits recipe
        """
        return reverse('recipe_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    """
    Model for Comment
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        To display the comments by created_on in ascending order
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
