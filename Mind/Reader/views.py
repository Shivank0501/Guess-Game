from django.shortcuts import render
from random import randint

def index(request):
    context = {}
    show_answer = False

    if 'answer' not in request.session:
        request.session['answer'] = randint(1, 100)
        request.session['attempts'] = 0

    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        answer = request.session.get('answer')
        attempts = request.session.get('attempts')
        request.session['attempts'] = attempts + 1 if attempts is not None else 1

        if guess < answer:
            context['message'] = 'Too low! Try again.'
        elif guess > answer:
            context['message'] = 'Too high! Try again.'
        else:
            context['message'] = 'Congratulations! You guessed it!'
            request.session.pop('answer')
            request.session.pop('attempts')

        if attempts and attempts >= 3:
            show_answer = True

    context['show_answer'] = show_answer
    context['answer'] = request.session.get('answer')

    return render(request, 'index.html', context)
