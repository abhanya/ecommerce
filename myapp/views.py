from django.shortcuts import render

# Create your views here.
def myapp_index (request):
    return render(request,'fold/index.html')