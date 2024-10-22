from django.shortcuts import render

# Create your views here.
def indexData(request):
    return render(request, 'empleadosApp/index.html')