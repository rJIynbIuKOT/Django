from django.shortcuts import render

from books.models import Publisher, Author, Book

def index(request):
    pubs = Publisher.objects.all()
    auts = Author.objects.all()
    context = {
        'pubs': pubs,
        'auts': auts
    }
    return render(request, 'books.html', context)
