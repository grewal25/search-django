from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic import TemplateView
from home.models import Book
from django.db.models import Q

# Create your views here.
class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'home/book_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(name__icontains = query) | Q(name__icontains = query) )

class HomePage(TemplateView):
    template_name = 'home/home.html'
    
    # queryset = Book.objects.filter(name__icontains = 'knowledge')