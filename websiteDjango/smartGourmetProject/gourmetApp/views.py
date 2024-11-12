from django.shortcuts import render

# Create your views here.
def indexData(request):
    return render(request, 'gourmetApp/index.html')

def contactos(request):
    return render(request, 'gourmetApp/contacts.html')