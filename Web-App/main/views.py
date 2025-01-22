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


        return render(request, 'admin/Admin.html')
    else:
        return render(request, 'admin/Error.html')
def ApplicationsForm(request):
    '''Форма заявки на получение'''
    #logging.info()
    g = list(Goods.objects.all())
    r = list(Applications_get.objects.all())

    user_name = User.objects.get(username=request.user)
    n = Applications_get.objects.filter(username=user_name)

    if request.method == 'POST':

        form = AddPostForm_get(request.POST or None, user=request.user)
        if form.is_valid():
            try:
                item = form.cleaned_data['Request']

                if int(form.data['Request_count']) <= Goods.available_count(self=item):
                    Applications_get.objects.create(**form.cleaned_data)
                    return  redirect('application-get')

                else:
                    error = 'Убедитесь, что инвентаря достаточно'
                    return render(request, 'main/Application.html', {'form': form ,'n' : n,'g' : g,'error': error })
            except:
                form.add_error(None,'Ошибка')
    else:
        form=AddPostForm_get(user=request.user)



    return render(request, 'main/Application.html' , {'form': form ,'n' : n,'g' : g})

def ApplicationsForm2(request):
    '''Форма заявки на ремонт'''
    #logging.info()
    g = list(Goods.objects.all())
    r = list(Applications_repair.objects.all())
    n = []
    for el in r:
        if request.user.username == el.username:
            n.append(el)
    if request.method == 'POST':

        form = AddPostForm_repair(request.POST or None, user=request.user)
        if form.is_valid():
            try:
                Applications_repair.objects.create(**form.cleaned_data)
                return  redirect('application-repair')
            except:
                form.add_error(None,'Ошибка')
    else:
        form=AddPostForm_repair(user=request.user)

    return render(request, 'main/Application2.html' , {'form': form,'n' : n})
def page(request):
    ''' Главная страница (просмотр инвентаря)'''
    Items = list(Goods.objects.all())
    for el in Items:
        el.count=Goods.available_count(self=el)
    return render(request, 'main/index.html' , {'Items': Items})
# console/add-purchase-plan/
def add_purchase_plan(request):
    ''' Добавления плана закупок'''
    if request.user.is_superuser:
        if request.method == "POST":
            form = PurchasePlanForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_purchase_plan')
        else:
            form = PurchasePlanForm()
        return render(request, 'admin/add_purchase_plan.html', {'form': form})
    else:
        return render(request, 'admin/Error.html')

# console/purchase-plan-list/
def purchase_plan_list(request):
    ''' Просмотр плана закупок'''
    if request.user.is_superuser:
        # Получаем все записи из модели PurchasePlan
        plans = PurchasePlan.objects.select_related('item', 'supplier').all()
        return render(request, 'admin/purchase_plan_list.html', {'plans': plans})
    else:
        return render(request, 'admin/Error.html')
# console/edit-inventory
def edit_inventory(request):
    ''' Добавление + просмотр инвентаря'''
    if request.user.is_superuser:
        g = list(Goods.objects.all())

        if request.method == "POST":
            form = EditGoodsForm(request.POST)
            if form.is_valid():
                try:
                    Goods.objects.create(**form.cleaned_data)
                    return redirect('edit_inventory')

                except:
                    form.add_error(None, 'Ошибка')
        else:
            form = EditGoodsForm()

        return render(request, 'admin/edit_inventory.html', {'form': form ,'g':g})
    else:
        return render(request, 'admin/Error.html')
def Update_inventory(request,post_id):
    '''Изменение инвентаря'''
    if request.user.is_superuser:
        g = list(Goods.objects.filter(pk=post_id))

        return render(request, 'admin/update_inventory.html', {'g': g})
    else:
        return render(request, 'admin/Error.html')
def Delete_inventory(request,post_id):
    ''' Удаление инвентаря'''
    if request.user.is_superuser:
        g = (Goods.objects.filter(pk=post_id))
        a = list(Applications_get.objects.all())
        #удаление заявок если в них есть инвентарь , который требуется удалить
        for i in g:
            for el in a:
                if (str(el.Request) == str(i.goods)):
                    el.delete()

        g.delete()
        return redirect('edit_inventory')
    else:
        return render(request, 'admin/Error.html')
def Request_for_receipt_inventory(request):
    ''' Посмотр заявок на получение'''
    if request.user.is_superuser:
        a = list(Applications_get.objects.all())
        return render(request, 'admin/request_for_receipt.html', {'a': a})
    else:
        return render(request, 'admin/Error.html')
def Update_Request_for_receipt_inventory(request,post_id):
    '''Изменение заявок на получение'''
    if request.user.is_superuser:
        a = list(Applications_get.objects.filter(pk=post_id))
        return render(request, 'admin/update_request_for_receipt.html', {'a': a})
    else:
        return render(request, 'admin/Error.html')
def Delete_Request_for_receipt_inventory(request,post_id):
     '''Удаление заявок на получение'''
     if request.user.is_superuser:
        a = (Applications_get.objects.filter(pk=post_id))
        a.delete()
        return redirect('Request_for_receipt_inventory')
     else:
        return render(request, 'admin/Error.html')



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