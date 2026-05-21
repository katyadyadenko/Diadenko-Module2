from django.test import TestCase
from .models import Category, Recipe


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Desserts")

        self.assertEqual(category.name, "Desserts")
        self.assertEqual(str(category), "Desserts")
        self.assertEqual(list(category), ["Desserts"])


class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main dishes")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Pasta",
            description="Simple pasta recipe",
            instructions="Boil pasta and add sauce",
            ingredients="Pasta, tomato sauce, cheese",
            category=self.category
        )

        self.assertEqual(recipe.title, "Pasta")
        self.assertEqual(str(recipe), "Pasta")
        self.assertEqual(recipe.category, self.category)

    def test_recipe_dates_are_created(self):
        recipe = Recipe.objects.create(
            title="Salad",
            description="Fresh salad",
            instructions="Cut vegetables and mix",
            ingredients="Tomato, cucumber, lettuce",
            category=self.category
        )

        self.assertIsNotNone(recipe.created_at)
        self.assertIsNotNone(recipe.updated_at)