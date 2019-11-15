from django.shortcuts import render, get_object_or_404

from books.models import Publisher, Author, Book

from .forms import AddBook
from django.shortcuts import redirect

def index(request):
    pubs = Publisher.objects.order_by('name')
    auts = Author.objects.order_by('name')
    bks = Book.objects.order_by('name')
    context = {
        'pubs': pubs,
        'auts': auts,
        'bks': bks
    }
    return render(request, 'books.html', context)

def book_page(request, pk):
    book = get_object_or_404(Book, pk=pk)
    bks = Book.objects.order_by('name')
    context = {
        'book': book,
        'bks': bks
    }
    return render(request, 'book_page.html', context)

def book_new(request):
    if request.method == "POST":
        form = AddBook(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('book_page', pk=post.pk)
    else:
        form = AddBook()
    return render(request, 'book_edit.html', {'form': form})

def book_edit(request, pk):
    post = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = AddBook(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('book_page', pk=post.pk)
    else:
        form = AddBook(instance=post)
    return render(request, 'book_edit.html', {'form': form})

def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('/books/')