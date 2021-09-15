from django.shortcuts import render
from .models import Medicine
# Create your views here.
def homeView(request):
    medicines=Medicine.objects.all().order_by('-name')
    return render(request,'index.html',{'medicines':medicines})