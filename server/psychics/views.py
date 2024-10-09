from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import UserNumberForm
from .psychic import Psychic
from .psychic_manager import PsychicManager


class Start(TemplateView):
    template_name = 'psychics/start.html'

    def post(self, request):
        if request.method == 'POST':
            if 'yes' in request.POST:
                return redirect('about')
            elif 'no' in request.POST:
                return redirect('finish')

        return render(request, self.template_name)


class About(TemplateView):
    template_name = 'psychics/about.html'

    def post(self, request):
        if request.method == 'POST':
            if 'confirm' in request.POST:
                return redirect('index')

        return render(request, self.template_name)


class Index(TemplateView):
    template_name = 'psychics/index.html'

    def get(self, request, *args, **kwargs):
        if 'psychics' not in request.session:
            psychics = [Psychic('Экстра-Саня'), Psychic('Всевидящий Борис')]
            request.session['psychics'] = PsychicManager(psychics).to_dict()
            request.session['user_numbers'] = []

        psychic_manager = PsychicManager.from_dict(request.session['psychics'])
        user_numbers = request.session['user_numbers']

        psychic_manager.make_guesses()
        request.session['psychics'] = psychic_manager.to_dict()

        form = UserNumberForm()
        return render(request, self.template_name, {
            'psychics': psychic_manager.psychics,
            'user_numbers': user_numbers,
            'form': form,
        })

    def post(self, request):
        if 'psychics' not in request.session:
            return redirect('index')

        psychic_manager = PsychicManager.from_dict(request.session['psychics'])
        user_numbers = request.session['user_numbers']

        if 'submit_number' in request.POST:
            form = UserNumberForm(request.POST)
            if form.is_valid():
                user_number = form.cleaned_data['user_number']
                user_numbers.append(user_number)
                psychic_manager.update_reliability(user_number)
                request.session['psychics'] = psychic_manager.to_dict()
                request.session['user_numbers'] = user_numbers
                return redirect('reliability')
            else:
                return render(request, self.template_name, {
                    'psychics': psychic_manager.psychics,
                    'user_numbers': user_numbers,
                    'form': form,
                })

        elif 'repeat' in request.POST:
            request.session['user_numbers'] = []
            psychic_manager.reset_psychics()
            return redirect('about')

        elif 'clear_history' in request.POST:
            del request.session['psychics']
            del request.session['user_numbers']
            return redirect('index')

        request.session['psychics'] = psychic_manager.to_dict()
        request.session['user_numbers'] = user_numbers
        return redirect('index')

class Reliability(TemplateView):
    template_name = 'psychics/reliability.html'

    def get(self, request, *args, **kwargs):
        if 'psychics' not in request.session:
            return redirect('index')

        psychic_manager = PsychicManager.from_dict(request.session['psychics'])
        user_numbers = request.session['user_numbers']

        return render(request, self.template_name, {
            'psychics': psychic_manager.psychics,
            'user_numbers': user_numbers,
        })

    def post(self, request):
        if 'finish' in request.POST:
            del request.session['psychics']
            del request.session['user_numbers']
            return redirect('finish')

        elif 'repeat' in request.POST:
            return redirect('about')

        elif 'clear_history' in request.POST:
            del request.session['psychics']
            del request.session['user_numbers']
            return redirect('index')

class Finish(TemplateView):
    template_name = 'psychics/finish.html'