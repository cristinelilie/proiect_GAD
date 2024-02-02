from django.shortcuts import render, redirect
from .forms import ProductsForm
from .models import Products
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# class ProductsList(ListView):
#     model = Products
#     context_object_name = 'products'
#
# class ProductDetail(DetailView):
#     model = Products
#     context_object_name = 'product'
#     template_name = 'produse/product.html'



def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")

    context = {"loginform": form}
    return render(request, "produse/home-login.html", context=context)

def user_logout(request):
    auth.logout(request)
    return redirect("my-login")

def register(request):

    form = CreateUserForm()
    if request.method == "POST":

        form =CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('my-login')
    context = {'registerform': form}
    return render(request, 'produse/register.html', context=context)


@login_required(login_url="my-login")
def home(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = ProductsForm(request.POST or None)
            if form.is_valid():
                new_product = Products.objects.create(
                    user=User.objects.get(pk=request.user.id),
                    product=form.cleaned_data["product"],
                    description=form.cleaned_data["description"],
                )
                form = ProductsForm()
                products = Products.objects.filter(user=request.user)
                buy_products = products.filter(cumparat=False).count()
                bought = products.filter(cumparat=True).count()
                context = {'form': form, 'products': products, 'buy': buy_products, 'bought': bought}
                return render(request, 'produse/home.html', context)
    else:
        form = ProductsForm()
        products = Products.objects.filter(user=request.user)
        buy_products = products.filter(cumparat=False).count()
        bought = products.filter(cumparat=True).count()
        context = {'form': form, 'products': products, 'buy': buy_products, 'bought':bought}
        return render(request, 'produse/home.html', context)


@login_required(login_url="my-login")
def update(request, id):
    product = Products.objects.get(pk=id)

    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        context = {'product':form}
        if form.is_valid():
            form.save()
            return render(request, 'produse/update.html', context)
    else:
        form = ProductsForm(instance=product)

    context = {'product': form}
    return render(request, 'produse/update.html', context)

@login_required(login_url="my-login")
def delete(request, id):
    product= Products.objects.get(pk=id)
    product.delete()
    return redirect('home')

@login_required(login_url="my-login")
def detail(request, id):
    product = Products.objects.get(pk=id)
    context = {'product': product}
    return render(request, 'produse/product.html', context)

@login_required(login_url="my-login")
def change_status(request, id):
    product = Products.objects.get(pk=id)
    if product.cumparat:
        product.cumparat = False
        product.save()
    else:
        product.cumparat =True
        product.save()
    return redirect('home')



def about(request):
    return render(request, 'produse/about.html')


