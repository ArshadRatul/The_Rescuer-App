from django.shortcuts import render

# Create your views here.
def generalpage(request):
    return render(request,'general/generalPage.html')