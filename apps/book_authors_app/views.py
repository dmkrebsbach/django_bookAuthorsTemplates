from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    return redirect("/books")



def books(request):
    bookDict = {}
    bookDict["books"] = Book.objects.all()
    bookDict["authors"] = Author.objects.all()
    return render(request, "book_authors_app/books.html", bookDict)

def createBook(request):
    if request.method == "POST":
        bookNew = Book.objects.create(
            title = request.POST["bookTitle"],
            desc = request.POST["bookDesc"]
        )
        bookNew.save()
    return redirect("/books")

def showBook(request, bookId):
    bookDictShow = {}
    bookDictShow["bookShow"] = Book.objects.get(id=bookId)
    bookDictShow["bookAuthors"] = Book.objects.get(id=bookId).authors.all()
    bookDictShow["books"] = Book.objects.all()
    bookDictShow["notAuthors"] = Author.objects.exclude(books = bookId)
    return render(request, "book_authors_app/showBook.html", bookDictShow)

def updateBook(request, bookId):
    if request.method == "POST":
        bookUpdate = Book.objects.get(id=bookId)
        bookUpdate.title = request.POST["updateTitle"]
        bookUpdate.desc = request.POST["updateDesc"]
        bookUpdate.save()
    return redirect(f"/books/{bookId}")

def editBook(request, bookId):
    if request.method == "POST":
        book = Book.objects.get(id = bookId)
        print("**************************************************")
        request.POST["author"]
        author = Author.objects.get(id = request.POST["author"])
        book.authors.add(author)
    return redirect(f"/books/{bookId}")





def authors(request):
    authorDict = {}
    authorDict["authors"] = Author.objects.all()
    return render(request, "book_authors_app/authors.html", authorDict)

def createAuthor(request):
    if request.method == "POST":
        authorNew = Author.objects.create(
            first_name = request.POST["authorFirstName"],
            last_name = request.POST["authorLastName"],
            notes = request.POST["authorNotes"],
        )
        authorNew.save()
    return redirect("/authors")

def showAuthor(request, authorId):
    authorDictShow = {}
    authorDictShow["authorShow"] = Author.objects.get(id=authorId)
    authorDictShow["authorBooks"] = Author.objects.get(id=authorId).books.all()
    authorDictShow["authors"] = Author.objects.all()
    authorDictShow["notBooks"] = Book.objects.exclude(authors = authorId)
    return render(request, "book_authors_app/showAuthor.html", authorDictShow)

def updateAuthor(request, authorId):
    if request.method == "POST":
        authUpdate = Author.objects.get(id = authorId)
        authUpdate.first_name = request.POST["updateFirstName"]
        authUpdate.last_name = request.POST["updateLastName"]
        authUpdate.notes = request.POST["updateNotes"]
        authUpdate.save()
    return redirect(f"/authors/{authorId}")

def editAuthor(request, authorId):
    if request.method == "POST":
        author = Author.objects.get(id = authorId)
        book = Book.objects.get(id = request.POST["book"])
        author.books.add(book)
    return redirect(f"/authors/{authorId}")