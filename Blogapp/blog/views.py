from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Shriya',
        'title': 'Blog post',
        'content': 'First post conten',
        'date-posted': 'November 14th, 2022'
    },
    {
        'author': 'Maithri',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date-posted': 'November 15th, 2022'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')