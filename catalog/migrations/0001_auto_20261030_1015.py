from django.db import migrations

def seed_books(apps, schema_editor):
    Author = apps.get_model("catalog", "Author")
    Book = apps.get_model("catalog", "Book")
    Genre = apps.get_model("catalog", "Genre")
    
    # Create an author
    adams = Author.objects.create(first_name="Douglas", last_name="Adams")
    
    # Create a book
    hitchhiker = Book.objects.create(
        title="Hitchhiker's Guide to the Galaxy",
        summary="A comedic sci-fi adventure.",
        isbn="9780330258647"
    )
    # Add relationship
    hitchhiker.author = adams
    hitchhiker.save()

class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(seed_books),
    ]