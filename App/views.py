from django.shortcuts import render,get_object_or_404
from .models import Medicine
from django.core.paginator import Paginator

# Create your views here.


def homeView(request):
    medicines = Medicine.objects.all().order_by('name')
    paginator = Paginator(medicines,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)

def detailsView(request,id):
    print(request)
    medicine = Medicine.objects.get(id=id)
    medicine = get_object_or_404(Medicine, pk=id)
    print('Medicine-----',medicine)

    return render(request,'details.html',{'medicine':medicine})
