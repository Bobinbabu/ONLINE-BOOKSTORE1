from django.shortcuts import render, redirect, get_object_or_404
from.models import *

def index(request):
    a = book.objects.all()
    return render(request, 'index.html', {'data':a})

def onlinebook(request):
    if request.method == 'POST':
        title = request.POST['Titilename']
        name = request.POST['Authorname']
        genre = request.POST['Genre']
        description = request.POST['Description']
        price = request.POST['Price']
        pb = request.POST['date']
        rate = request.POST['rate']
        data = book(
            Titlename = title,
            Authorname = name,
            Genre = genre,
            Description = description,
            Price = price,
            Publisheddate = pb,
            Rate = rate
        )
        data.save()
        return redirect('/index')
    
def delete1(request,id):
    dele = book.objects.get(id=id)
    dele.delete()
    return redirect('/index')

def edit(request,id):
    edit1 = get_object_or_404(book, id=id)
    if request.method == 'POST':
        title = request.POST['Titilename']
        name = request.POST['Authorname']
        genre = request.POST['Genre']
        description = request.POST['Description']
        price = request.POST['Price']
        pb = request.POST['date']
        edit1.Titlename = title
        edit1.Authorname = name
        edit1.Genre = genre
        edit1.Description = description
        edit1.Price = price
        edit1.Publisheddate = pb
        edit1.save()
        return redirect('/index')
    return render(request, 'edit.html', {'edit1':edit1})

