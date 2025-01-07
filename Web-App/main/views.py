from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView

from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .utils import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

def AdminPage(request):
    if request.user.is_superuser:
        g = list(Goods.objects.all())
        u = list(Users.objects.all())
        U2 = []
        for el in u:
            U2.append(el.Rent)


        for el2 in g:
            for el in u:
                if el2 == el.Rent and el.Plus == False:
                    el2.rented_count += el.Count
                    el.Plus = True
                    el2.save()
                    el.save()

        for el2 in g:
            if not (el2 in U2):
                el2.rented_count = 0
                el2.save()
                
        return render(request, 'main/Admin.html')
def ApplicationsForm(request):

    #logging.info()
    g = list(Goods.objects.all())
    r = list(Applications.objects.all())
    n = []
    for el in r:
        if request.user.username == el.username:
            n.append(el)
    if request.method == 'POST':

        form = AddPostFormR(request.POST or None, user=request.user)
        if form.is_valid():
            try:
                item = int(form.data['Request'])
                rented_counts = []
                counts = []
                for el in g:
                    rented_counts.append(el.rented_count)
                    counts.append(el.count)
                if int(form.data['Request_count']) <= (counts[item-1] - rented_counts[item-1]):
                    Applications.objects.create(**form.cleaned_data)
                    return  redirect('application')

                else:
                    error = 'Убедитесь, что инвентаря достаточно'
                    return render(request, 'main/Application.html', {'form': form ,'n' : n,'g' : g,'error': error })
            except:
                form.add_error(None,'Ошибка')
    else:
        form=AddPostFormR(user=request.user)



    return render(request, 'main/Application.html' , {'form': form ,'n' : n,'g' : g})

def page(request):
    Items = list(Goods.objects.all())
    for el in Items:
        el.count=el.count-el.rented_count
    return render(request, 'main/index.html' , {'Items': Items})


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')



def logout_user(request):
    logout(request)
    return redirect('login')
