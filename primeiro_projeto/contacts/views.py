from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    return render(
        request,
        'contacts/index.html'
    )
