from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Car, Customer
from .forms import CarForm, CustomerForm, HwLoginForm
from django.urls import reverse, reverse_lazy

class CarsView(View):
    def get(self, request):
        cars =  Car.objects.all()
        ctx = {
            'cars': cars,
        }
        return render(request, 'cars.html', ctx)

class CarView(View):
    def get(self, request, id):
        car = Car.objects.get(id=id)
        ctx = {
            'car': car,
        }
        return render(request,'car.html',ctx)

class UpdateCarView(View):
    def get(self, request, id):
        car = Car.objects.get(pk=id)
        form = CarForm(instance=car)
        ctx = {
            'form': form,
        }
        return render(request, 'update_car.html', ctx)
    def post(self, request, id):
        car = Car.objects.get(pk=id)
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return HttpResponse('Dane zmodifikowano')

class AddCarView(View):

    def get(selfs, reguest):
        ctx = {
            'form':CarForm,
        }
        return render(reguest, 'update_car.html',ctx)

    def post(self, request):
        form = CarForm(request.POST)
        if form.is_valid():
            Car.objects.create(**form.cleaned_data)
            return HttpResponse('Nowy samochód dodany')
        
# CUSTOMERS
class CustomersView(View):
    def get(self, request):
        customers =  Customer.objects.all()
        ctx = {
            'customers': customers,
        }
        return render(request, 'customers.html', ctx)
    
class CustomerView(View):
    def get(self, request, id):
        customer = Customer.objects.get(id=id)
        ctx = {
            'customer': customer,
        }
        return render(request,'customer.html',ctx)
    
    
class UpdateCustomerView(View):
    def get(self, request, id):
        customer = Customer.objects.get(pk=id)
        form = CustomerForm(instance=customer)
        ctx = {
            'form': form,
        }
        return render(request, 'update_customer.html', ctx)
    def post(self, request, id):
        customer = Customer.objects.get(pk=id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponse('Dane zmodifikowano')

class AddCustomerView(View):

    def get(selfs, reguest):
        ctx = {
            'form':CustomerForm,
        }
        return render(reguest, 'update_customer.html',ctx)

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
            return HttpResponse('Dodano nowego klienta')
        
        
# LOGIN
class HwLoginView(View):
    def get(self, request):
        ctx = {
            'form': HwLoginForm(),
        }
        return render(request, 'hwlogin.html', ctx)
    def post(self, request):
        form = HwLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                url = request.GET.get('next')
                if url:
                    return redirect(url)
                return HttpResponseRedirect(reverse('cars'))
            else:
                form.add_error(field=None, error='Zły login lub hasło')
        ctx = {
            'form': form,
        }
        return render(request, 'hwlogin.html', ctx)

class HwLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('Zostałeś wylogowany')