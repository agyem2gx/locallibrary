from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Challenge: counts for genres and books containing a word
    num_genres = Genre.objects.all().count()
    num_books_with_fiction = Book.objects.filter(title__icontains='fiction').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_fiction': num_books_with_fiction,
    }

    return render(request, 'index.html', context=context)