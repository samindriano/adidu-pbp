import datetime
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406400524',
        'name': request.user.username,
        'class': 'PBP B',
        'product_list' : product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")
    
def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'category_display': product.get_category_display(),
            'is_featured': product.is_featured,
            'brand': product.brand,
            'stock': product.stock,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        # Ambil data produk dengan user terkait
        product = Product.objects.select_related('user').get(pk=product_id)
        
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'brand': product.brand,
            'stock': product.stock,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:  # [MODIFIED] ganti News → Product
        return JsonResponse({'detail': 'Not found'}, status=404)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    brand = request.POST.get("brand")
    stock = request.POST.get("stock")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user if request.user.is_authenticated else None

    new_product = Product(
        user=user,
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        brand=brand,
        stock=stock,
        is_featured=is_featured,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def update_product_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.name = request.POST.get("name")
    product.price = request.POST.get("price")
    product.description = request.POST.get("description")
    product.thumbnail = request.POST.get("thumbnail")
    product.category = request.POST.get("category")
    product.brand = request.POST.get("brand")
    product.stock = request.POST.get("stock")
    product.is_featured = request.POST.get("is_featured") == 'on'
    product.save()

    return HttpResponse(b"UPDATED", status=200)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_product_ajax(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return HttpResponse(b"DELETED", status=200)

@csrf_exempt
@require_POST
def login_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = JsonResponse({'redirect': reverse("main:show_main")})
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'redirect': reverse("main:login")})
    return JsonResponse({'errors': form.errors}, status=400)