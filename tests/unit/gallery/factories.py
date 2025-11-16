"""Factories for generating test data."""

import factory

from gallery.models import Category, Photo


class CategoryFactory(factory.django.DjangoModelFactory):
    """Factory for creating Category test objects."""

    class Meta:
        model = Category

    name = factory.Faker("word")


class PhotoFactory(factory.django.DjangoModelFactory):
    """Factory for creating Photo test objects."""

    class Meta:
        model = Photo

    title = factory.Faker("sentence", nb_words=4)
    image = factory.django.ImageField(color="blue", width=400, height=300)
    category = factory.SubFactory(CategoryFactory)
