"""Tests for gallery views."""

import pytest
from django.test import Client
from django.urls import reverse

from tests.unit.gallery.factories import CategoryFactory, PhotoFactory


@pytest.mark.django_db
class TestGalleryViews:
    """Tests for gallery views."""

    def setup_method(self):
        """Set up test client and data."""
        self.client = Client()

    def test_gallery_home_view(self):
        """Test the gallery home view."""
        category = CategoryFactory(name="Nature")
        response = self.client.get(reverse("gallery_home"))

        assert response.status_code == 200
        assert "gallery/gallery.html" in [t.name for t in response.templates]
        assert category in response.context["categories"]

    def test_gallery_home_empty(self):
        """Test the gallery home view with no categories."""
        response = self.client.get(reverse("gallery_home"))

        assert response.status_code == 200
        assert len(response.context["categories"]) == 0

    def test_gallery_category_view(self):
        """Test the gallery category view."""
        category = CategoryFactory(name="Landscapes")
        photo1 = PhotoFactory(category=category, title="Photo 1")
        photo2 = PhotoFactory(category=category, title="Photo 2")

        response = self.client.get(
            reverse("gallery_category", args=[category.id])
        )

        assert response.status_code == 200
        assert response.context["category"] == category
        assert photo1 in response.context["photos"]
        assert photo2 in response.context["photos"]

    def test_gallery_category_not_found(self):
        """Test the gallery category view with invalid category ID."""
        with pytest.raises(Exception):
            self.client.get(reverse("gallery_category", args=[999]))

    def test_hobbies_view(self):
        """Test the hobbies view."""
        response = self.client.get(reverse("hobbies"))

        assert response.status_code == 200
        assert "gallery/hobbies.html" in [t.name for t in response.templates]

    def test_homepage_view(self):
        """Test the homepage view."""
        response = self.client.get(reverse("homepage"))

        assert response.status_code == 200
        assert "gallery/homepage.html" in [t.name for t in response.templates]

    def test_personal_view(self):
        """Test the personal view."""
        response = self.client.get(reverse("personal"))

        assert response.status_code == 200
        assert "gallery/personal.html" in [t.name for t in response.templates]
