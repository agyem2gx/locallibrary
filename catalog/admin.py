from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language, BookAuthor

# Simple registrations
admin.site.register(Genre)
admin.site.register(Language)

# Inlines
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookAuthorInline(admin.TabularInline):
    model = BookAuthor
    extra = 1

# Admins
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookAuthorInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre', 'language')
    inlines = [BooksInstanceInline, BookAuthorInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
    )

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author', 'author_order')