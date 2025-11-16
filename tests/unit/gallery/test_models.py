"""Tests for gallery models."""

import pytest

from gallery.models import Category, Photo
from tests.unit.gallery.factories import CategoryFactory, PhotoFactory


@pytest.mark.django_db
class TestCategoryModel:
    """Tests for the Category model."""

    def test_create_category(self):
        """Test creating a category."""
        category = CategoryFactory(name="Nature")
        assert category.id is not None
        assert category.name == "Nature"

    def test_category_str(self):
        """Test the string representation of a category."""
        category = CategoryFactory(name="Architecture")
        assert str(category) == "Architecture"

    def test_category_ordering(self):
        """Test that categories can be retrieved from the database."""
        category1 = CategoryFactory(name="Landscapes")
        category2 = CategoryFactory(name="Urban")

        categories = Category.objects.all()
        assert categories.count() == 2
        assert category1 in categories
        assert category2 in categories


@pytest.mark.django_db
class TestPhotoModel:
    """Tests for the Photo model."""

    def test_create_photo(self):
        """Test creating a photo."""
        category = CategoryFactory()
        photo = PhotoFactory(title="Beautiful Sunset", category=category)

        assert photo.id is not None
        assert photo.title == "Beautiful Sunset"
        assert photo.category == category

    def test_photo_str(self):
        """Test the string representation of a photo."""
        photo = PhotoFactory(title="Mountain View")
        assert str(photo) == "Mountain View"

    def test_photo_category_relationship(self):
        """Test the relationship between Photo and Category."""
        category = CategoryFactory(name="Landscapes")
        photo1 = PhotoFactory(category=category, title="Photo 1")
        photo2 = PhotoFactory(category=category, title="Photo 2")

        photos_in_category = Photo.objects.filter(category=category)
        assert photos_in_category.count() == 2
        assert photo1 in photos_in_category
        assert photo2 in photos_in_category

    def test_delete_category_deletes_photos(self):
        """Test that deleting a category deletes its photos."""
        category = CategoryFactory()
        photo = PhotoFactory(category=category)

        category.delete()
        assert Photo.objects.filter(id=photo.id).count() == 0
