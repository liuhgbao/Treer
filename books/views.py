from django.shortcuts import render_to_response
from django.template import RequestContext
from books.models import Book
# Create your views here.

def bs(request):
    booklist=Book.objects.all().order_by('-publication_date')
    return render_to_response('booksshare.html',{'booklist':booklist})
