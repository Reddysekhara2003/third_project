from django.shortcuts import render

# Create your views here.
def book(request):
    return render(request,'book.html')
def pen(request):
    return render(request,'pen.html')