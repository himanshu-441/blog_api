from django.shortcuts import render
import requests, json


# Create your views here.
def home(request):
    a = requests.get("http://127.0.0.1:8000/api/posts")
    data=a.json()
    b = requests.get("http://127.0.0.1:8000/api/comments")
    b = b.json()
    
    context = {
        'data':data,
        'comments': b,
    }
    return render(request, 'home.html', context)
    

