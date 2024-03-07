from django.http import HttpResponse
from django.shortcuts import render
from  .forms import CandidateForm
from django.contrib.auth.models import User
from .models import  Exam

def home(request):
    user = request.user
    return render(request, 'exam/home.html', {'user': user})

# Create your views here.
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
           #recibir datos
            firts_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name'] 
            user_name = form.cleaned_data['user_name'] 
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password'] 
            career = form.cleaned_data['career'] 
            stage = form.cleaned_data['stage'] 

           #crear usuario 
            user = User.objects.create_user(user_name,email,password)
            user.last_name = last_name
            user.save()

           #crear examen 
            exam = Exam.objects.create(user=user, career=career, stage=stage)
            exam.save()
           #recibir datos 
        exam.set_modules()
        exam.set_questions()
        return HttpResponse("Usuario y examen creados")
    form = CandidateForm()
    return render(request,
                  'exam/add_candidate.html',
                  {'form': form})
