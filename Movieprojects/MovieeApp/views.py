from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Moviesform
from .models import Movies


# Create your views here.
def Docs(request):
    movies=Movies.objects.all
    context={
        'Movies_list':movies
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movies=Movies.objects.get(id=movie_id)
    return render(request,"detail.html",{'movies':movies})
def add_movies(request):
    if request.method =='POST':
        name=request.POST.get('name',)
        Desc=request.POST.get('Desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movies=Movies(name=name,Desc=Desc,year=year,img=img)
        movies.save()
    return render(request,'add.html')
def update(request,id):
    movies=Movies.objects.get(id=id)
    form=Moviesform(request.POST or None, request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movies':movies})
def delete(request,id):
    if request.method=='POST':
        movies = Movies.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')





