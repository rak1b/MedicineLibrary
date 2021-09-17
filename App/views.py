from django.shortcuts import render,get_object_or_404,redirect
from .models import Medicine
from django.core.paginator import Paginator
from django.db.models import Q 

from django.contrib.auth import login, authenticate,logout

from .forms import SignUpForm,loginForm
from django.contrib import messages


def homeView(request):
    medicines = Medicine.objects.all().order_by('name')
    paginator = Paginator(medicines,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)

def detailsView(request,id,name):
    print(request)
    medicine = get_object_or_404(Medicine, pk=id)
    
    related_medicine = Medicine.objects.filter(group__name = medicine.group.name)
    context = {
        'medicine':medicine,
        'related_medicine':related_medicine,
        'med_len':len(related_medicine)
        }

    return render(request,'details.html',context)

def testView(request):
    medicines = Medicine.objects.all().order_by('name')

    context = {
        'medicine':medicines,
        }
    return render(request,'test2.html',context)

def searchView(request):
    query = request.GET.get('q')
    search_meds = Medicine.objects.filter(Q(name__icontains=query) | Q(group__name__icontains=query))
    check_empty = len(search_meds)
    context = {
        'search_meds':search_meds,
        'query' : query,
        'len':check_empty
        
        }
    return render(request,'search.html',context)

def signupView(request):
    if request.method == 'POST': #if the form has been submitted
        form = SignUpForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('loginView')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('homeView')

    return render(request, 'login.html')


def logoutView(request):
    logout(request)

