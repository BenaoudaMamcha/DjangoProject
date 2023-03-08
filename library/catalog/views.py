from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import  Book, Author, BookInstance , Genre , Language
from django.views.generic import CreateView , DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# 

from django.contrib.auth.forms import UserCreationForm


# Create your views here.



def index(request):
    
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_avail=BookInstance.objects.filter(status__exact='a').count()
     
    context = {
        'num_books': num_books, 
        'num_instances' : num_instances,
        'num_instances_avail' : num_instances_avail
    }
    
     # Render the HTML template index.html with the data in the context variable
    return render(request,'catalog/index.html',context=context)

class BookCreate(LoginRequiredMixin ,CreateView): # book_form.html
    model= Book
    fields='__all__'


class BookDetail( DetailView):
    model = Book


@login_required
def my_view(request):
    return render(request,'catalog/my_view.html')

 # registration code
 
class SignUpView(CreateView):
    
     form_class = UserCreationForm
     
     success_url= reverse_lazy('login')
     
     template_name= 'catalog/signup.html'
 
 
 # create a specif view for filter list of book tha are borrowed by the current user
 
class CheckedoutBookUserView(LoginRequiredMixin, ListView):
    #list all book instances
    
    model = BookInstance
    
    template_name = 'catalog/profile.html'
    
    paginate_by= 5 # nb pbook a affiché par page
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
    
    