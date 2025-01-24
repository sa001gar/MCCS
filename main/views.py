from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def faculty(request):
    return render(request, 'main/faculty.html')

def team(request):
    return render(request, 'main/team.html')

def alumni(request):
    return render(request, 'main/alumni.html')

def gallery(request):
    return render(request, 'main/department-gallery.html')

def feedback(request):
    return render(request, 'main/feedback.html')