from django.shortcuts import render , redirect
from .forms import AddBookForm, EditBookForm
from .models import AddBook 

def Bookpage(request):
    return render(request, 'Book/books.html')

def Addbookpage(request):
    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            form.save()
            # Redirect to a success URL after saving the form
            #return redirect('success')  # Replace 'success' with the actual name of your success URL
            return redirect('Book:Booklistpage')
    else:
        # If the request method is not POST, create a new form instance
        form = AddBookForm()
    
    # Render the form initially or when the request method is not POST
    return render(request, "Book/Addbook.html", {'add_book': form})

#list of books
def Booklistpage(request): 
    list_book = AddBook.objects.all().order_by('book_name')
    return render(request, 'Book/booklist.html', {'list_book': list_book})
    
#delete book
def Deletebook(request, id):
    delete_book = AddBook.objects.get(id=id)
    delete_book.delete()
    return redirect('Book:Booklistpage')

#edit Book
def Editbookpage(request, id):
    edit_book = AddBook.objects.get(id=id)
    return render(request, 'Book/editbook.html', {'edit_book': edit_book})

def Editbook(request, id):
    edit_book = AddBook.objects.get(id=id)
    form = EditBookForm (request.POST, request.FILES, instance=edit_book)
    if form.is_valid():
        form.save()
        return redirect('Book:Booklistpage')

def Bookdetail(request, id):
    book = AddBook.objects.get(id=id)
    return render(request, 'Book/bookdetail.html', {'book': book})
