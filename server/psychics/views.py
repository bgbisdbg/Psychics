from django.shortcuts import render, redirect
from .psychic import Psychic
from .forms import UserNumberForm

def index(request):
    if 'psychics' not in request.session:
        psychics = [Psychic('Psychic 1'), Psychic('Psychic 2')]
        request.session['psychics'] = [p.to_dict() for p in psychics]
        request.session['user_numbers'] = []

    psychics = [Psychic.from_dict(p) for p in request.session['psychics']]
    user_numbers = request.session['user_numbers']

    if request.method == 'POST':
        if 'confirm' in request.POST:
            for psychic in psychics:
                psychic.make_guess()
        elif 'submit_number' in request.POST:
            form = UserNumberForm(request.POST)
            if form.is_valid():
                user_number = form.cleaned_data['user_number']
                user_numbers.append(user_number)
                for psychic in psychics:
                    psychic.update_reliability(user_number)
            else:
                return render(request, 'test_app/index.html', {
                    'psychics': psychics,
                    'user_numbers': user_numbers,
                    'form': form,
                })
        elif 'clear_history' in request.POST:
            del request.session['psychics']
            del request.session['user_numbers']
            return redirect('index')

        request.session['psychics'] = [p.to_dict() for p in psychics]
        request.session['user_numbers'] = user_numbers
        return redirect('index')

    form = UserNumberForm()
    return render(request, 'psychics/index.html', {
        'psychics': psychics,
        'user_numbers': user_numbers,
        'form': form,
    })