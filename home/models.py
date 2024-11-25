from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    # Choices for the veg/non-veg field
    FOOD_TYPE_CHOICES = [
        ('Veg', 'Vegetarian'),
        ('Non-Veg', 'Non-Vegetarian'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    recipe_img = models.ImageField(upload_to="recipes")
    food_type = models.CharField(max_length=7, choices=FOOD_TYPE_CHOICES, default='Veg')
    steps = models.TextField(null=False)  # New field for recipe steps
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipe_name} ({self.food_type})"
