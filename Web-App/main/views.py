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

    user_name = User.objects.get(username=request.user)
    n = Applications_repair.objects.filter(username=user_name)

    if request.method == 'POST':

        form = AddPostForm_repiar(request.POST or None, user=request.user)
        if form.is_valid():
            try:
                Applications_repair.objects.create(**form.cleaned_data)
                return  redirect('application-repair')
            except:
                form.add_error(None,'Ошибка')
    else:
        form=AddPostForm_repiar(user=request.user)

    return render(request, 'main/Application2.html' , {'form': form,'n' : n})
def page(request):
    ''' Главная страница (просмотр инвентаря)'''
    Items = list(Goods.objects.all())
    for el in Items:
        el.count=Goods.available_count(self=el)

    return render(request, 'main/index.html' , {'Items': Items})
# console/add-purchase-plan/
def purchase_plan(request):
    ''' Добавления плана закупок'''
    if request.user.is_superuser:
        plans = PurchasePlan.objects.select_related('item', 'supplier').all()
        if request.method == "POST":
            form = PurchasePlanForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('purchase_plan')
        else:
            form = PurchasePlanForm()
        return render(request, 'admin/purchase_plan.html', {'form': form,'plans': plans})
    else:
        return render(request, 'admin/Error.html')

# console/purchase-plan/

def edit_inventory(request):
    ''' Добавление + просмотр инвентаря'''
    if request.user.is_superuser:
        g = list(Goods.objects.all())

        if request.method == "POST":
            form = UpdateGoodsForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('edit_inventory')
        else:
            form = UpdateGoodsForm()

        return render(request, 'admin/edit_inventory.html', {'form': form ,'g':g})
    else:
        return render(request, 'admin/Error.html')
def Update_inventory(request,post_id):
    '''Изменение инвентаря'''
    if request.user.is_superuser:
        g = (Goods.objects.get(pk=post_id))

        form = UpdateGoodsForm(request.POST or None, instance=g)
        if form.is_valid():
            form.save()
            return redirect('edit_inventory')


        return render(request, 'admin/update_inventory.html', {'form':form,'g': g})
    else:
        return render(request, 'admin/Error.html')
def Delete_inventory(request,post_id):
    ''' Удаление инвентаря'''
    if request.user.is_superuser:
        g = (Goods.objects.filter(pk=post_id))
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
        a = (Applications_get.objects.get(pk=post_id))

        form = Admin_AddPostForm_get(request.POST or None,instance=a)
        if form.is_valid():
            form.save()
            return redirect('Request_for_receipt_inventory')

        return render(request, 'admin/update_request_for_receipt.html', {'form':form,'a': a})
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

def Request_for_repair_inventory(request):
    '''Просмотр заявок на ремонт'''
    if request.user.is_superuser:
        a = (Applications_repair.objects.all())

        return render(request, 'admin/request_for_repair.html', {'a': a})
    else:
        return render(request, 'admin/Error.html')

def Update_Request_for_repair_inventory(request,post_id):
    '''Изменение заявок на ремонт или замену'''
    if request.user.is_superuser:
        a = (Applications_repair.objects.get(pk=post_id))

        form = Admin_AddPostForm_repiar(request.POST or None, instance=a)
        if form.is_valid():
            form.save()
            return redirect('Request_for_repair_inventory')

        return render(request, 'admin/update_request_for_repair.html', {'form':form,'a': a})
    else:
        return render(request, 'admin/Error.html')
def Delete_Request_for_repair_inventory(request,post_id):
    '''Удаление заявок на ремонт или замену'''
    if request.user.is_superuser:
        a = (Applications_repair.objects.filter(pk=post_id))
        a.delete()
        return redirect('Request_for_repair_inventory')
    else:
        return render(request, 'admin/Error.html')

def Inventory_management(request):
    '''Управление инвентарем (выдача инветаря)'''
    if request.user.is_superuser:
        u = (Users.objects.all())
        form = Form_Inventory_management(request.POST or None)
        if form.is_valid():
            item = form.cleaned_data['Rent']
            count = form.cleaned_data['Count']
            if int(count) <= Goods.available_count(self=item):
                Goods.rent_item(self=item,quantity=count)
                form.save()
            else:
                error = 'Убедитесь, что инвентаря достаточно'
                return render(request, 'admin/Inventory_management.html', {'form': form, 'u': u, 'error': error})
            return redirect('Inventory_management')

        return render(request, 'admin/Inventory_management.html', {'form':form,'u': u})
    else:
        return render(request, 'admin/Error.html')
def Inventory_management_delete(request,post_id):
    '''Удаление инвентаря у пользователей'''
    if request.user.is_superuser:
        u = (Users.objects.filter(pk=post_id))
        for el in u:
            item = el.Rent
            count = el.Count
            Goods.return_item(self=item,quantity=count)
        u.delete()
        return redirect('Inventory_management')
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