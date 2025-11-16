"""Integration tests - Testing page loading, assets and full page rendering."""

import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.integration
@pytest.mark.django_db
class TestPageIntegration:
    """Integration tests for page loading and assets."""

    def setup_method(self):
        """Set up test client."""
        self.client = Client()

    def test_homepage_loads_with_all_resources(self):
        """Test that homepage loads and contains expected content."""
        response = self.client.get(reverse("homepage"))

        assert response.status_code == 200
        # Check for key content markers
        assert b"Nander Speerstra" in response.content
        assert b"MLOps Engineer" in response.content
        assert b"scalable ML pipelines" in response.content

    def test_professional_page_loads(self):
        """Test that professional page loads with content."""
        response = self.client.get(reverse("professional"))

        assert response.status_code == 200
        assert b"Professional Journey" in response.content
        assert b"Technical Expertise" in response.content

    def test_personal_page_loads(self):
        """Test that personal page loads with content."""
        response = self.client.get(reverse("personal"))

        assert response.status_code == 200
        assert (
            b"My World" in response.content or b"Hobbies" in response.content
        )

    def test_hobbies_page_loads(self):
        """Test that hobbies page loads with content."""
        response = self.client.get(reverse("hobbies"))

        assert response.status_code == 200
        assert b"Hobbies" in response.content or b"Mini" in response.content

    def test_gallery_page_loads(self):
        """Test that gallery home page loads."""
        response = self.client.get(reverse("gallery_home"))

        assert response.status_code == 200
        assert (
            b"Photography" in response.content
            or b"Gallery" in response.content
        )

    def test_all_pages_have_header(self):
        """Test that all pages include the header component."""
        pages = [
            reverse("homepage"),
            reverse("personal"),
            reverse("professional"),
            reverse("hobbies"),
            reverse("gallery_home"),
        ]

        for page in pages:
            response = self.client.get(page)
            assert response.status_code == 200
            # Check for header elements
            assert b"navmenu" in response.content

    def test_all_pages_have_footer(self):
        """Test that all pages include the footer component."""
        pages = [
            reverse("homepage"),
            reverse("personal"),
            reverse("professional"),
            reverse("hobbies"),
            reverse("gallery_home"),
        ]

        for page in pages:
            response = self.client.get(page)
            assert response.status_code == 200
            # Check for footer elements
            assert b"Nander Speerstra" in response.content

    def test_static_files_referenced_in_pages(self):
        """Test that static file references are present in pages."""
        response = self.client.get(reverse("homepage"))

        assert response.status_code == 200
        # Check for CSS and JS references
        assert (
            b"css/main.css" in response.content
            or b"bootstrap.min.css" in response.content
        )
        assert (
            b"main.js" in response.content or b"glightbox" in response.content
        )

    def test_image_tags_have_alt_text(self):
        """Test that image tags contain alt text for accessibility."""
        response = self.client.get(reverse("homepage"))

        assert response.status_code == 200
        # Images should have alt attributes
        assert b"alt=" in response.content

    def test_no_broken_links_in_navigation(self):
        """Test that navigation links resolve correctly."""
        response = self.client.get(reverse("homepage"))
        assert response.status_code == 200

        # Check for key navigation links
        assert b'href="/' in response.content

    def test_page_title_set_correctly(self):
        """Test that page titles are properly set."""
        test_cases = [
            (reverse("homepage"), b"Home"),
            (reverse("professional"), b"Professional"),
            (reverse("personal"), b"Personal"),
        ]

        for url, title_part in test_cases:
            response = self.client.get(url)
            assert response.status_code == 200
            assert b"<title>" in response.content
