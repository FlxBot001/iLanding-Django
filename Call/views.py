from django.shortcuts import render

# Create your views here.

def home(request):
   return render(request, 'index.html')

def starter(request):
   return render(request, 'starter-page.html')

def service(request):
   return render(request, 'service-detail.html')
