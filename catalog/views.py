from django.shortcuts import render

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    #Modify the view to generate counts for genres and books that
        #contain a particular word (case insensitive)
    fantasy_count = Book.objects.filter(title__contains='fantasy').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'fantasy_count': fantasy_count,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
#the render() function will expect to find the file index.html
#in /locallibrary/catalog/templates/
#and will raise an error if the file is not present.

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book
