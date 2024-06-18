from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Question, Option
from django.urls import reverse
from .forms import QuizForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz_home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def quiz_home(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            total_score = calculate_total_score(form.cleaned_data)
            return HttpResponseRedirect(reverse('result', args=[total_score]))
    else:
        form = QuizForm(questions=questions)
    return render(request, 'quiz_home.html', {'form': form})

def calculate_total_score(cleaned_data):
    total_score = 0
    for key, value in cleaned_data.items():
        if key.startswith('question_'):
            question_id = key.split('_')[1]
            selected_option_id = value
            selected_option = get_object_or_404(Option, id=selected_option_id)
            if selected_option.is_correct:
                total_score += 5  
    return total_score

@login_required(login_url='login')
def result(request, total_score):
    return render(request, 'result.html', {'total_score': total_score})

@login_required(login_url='login')
def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        for question in Question.objects.all():
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id is not None and selected_option_id !='':
                selected_option = get_object_or_404(Option, id=selected_option_id)
                if selected_option.is_correct:
                    score += 5
        return JsonResponse({'score': score})
    return JsonResponse({'error': 'Invalid request'}, status=400)