from django.shortcuts import render,get_object_or_404,redirect
from .models import Medicine,Answer,Question
from django.core.paginator import Paginator
from django.db.models import Q 

from django.contrib.auth import login, authenticate,logout

from .forms import SignUpForm
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
    if query!="":
        search_meds = Medicine.objects.filter(Q(name__icontains=query) | Q(group__name__icontains=query))
        check_empty = len(search_meds)
        context = {
            'search_meds':search_meds,
            'query' : query,
            'len':check_empty
            
            }
        return render(request,'search.html',context)
    return render(request,'search.html',{'len':0})
    

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
            return redirect('homeView')
        else:
            messages.error(request, "Username or password is wrong,Please try again..")
    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect('homeView')

def forumView(request):
    which_ques = request.GET.get('questions')
    questions = Question.objects.all().order_by('-date_added')
    my_questions = Question.objects.filter(user=request.user).order_by('-date_added')
    print(questions)
    if which_ques=='my':
        paginator = Paginator(my_questions,6)
        title = 'Question You Have Asked'
    else:
        paginator = Paginator(questions,6)
        title = 'Question People Asked'
        
        
        
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'total_ques':len(questions),
        'total_my_ques':len(my_questions),
        'title':title
    }
    return render(request,'forum.html',context)

def ques_detailsView(request,id):
    question = Question.objects.get(id=id)
    answer = Answer.objects.filter(question__id=id)
    if request.method == "POST":
        ans = request.POST.get('answer_input')
        Answer.objects.create(answer=ans,user=request.user,question=question)
        
    context = {
    'ques':question,
    'answer':answer
    }

    return render(request,'ques_details.html',context)


def askView(request):
    if request.method == "POST":
        ques = request.POST.get('question_input')
        new_ques = Question.objects.create(question=ques,user=request.user)
        return redirect('forumView')
    
    context = {}
    return render(request,'ask.html',context)

