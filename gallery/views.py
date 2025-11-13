from django.shortcuts import render
from .models import Category, Photo


def gallery_home(request):
    categories = Category.objects.all()
    return render(request, "gallery/gallery.html", {"categories": categories})


def gallery_category(request, category_id):
    category = Category.objects.get(id=category_id)
    photos = Photo.objects.filter(category=category)
    return render(
        request,
        "gallery/gallery-category.html",
        {"category": category, "photos": photos},
    )


def homepage(request):
    return render(request, "gallery/homepage.html")


def personal(request):
    return render(request, "gallery/personal.html")


def professional(request):
    return render(request, "gallery/professional.html")
