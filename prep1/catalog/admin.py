from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Simple registrations for models with only one field
admin.site.register(Genre)
admin.site.register(Language)

# Author admin with list display and field layout
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

admin.site.register(Author, AuthorAdmin)

# Inline for BookInstance inside Book
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # no extra empty rows

# Book admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
    inlines = [BooksInstanceInline]

# BookInstance admin
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )

# Challenge: add Book inline to Author detail view
class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    # Don't show the ManyToMany field in the inline; keep it simple
    fields = ['title', 'isbn']

# We need to unregister the existing Author registration first
# because we already registered AuthorAdmin earlier.
admin.site.unregister(Author)
@admin.register(Author)
class AuthorAdminWithInline(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]