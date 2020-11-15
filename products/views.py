from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404

from .forms import ProductForm
from .models import Product


@login_required
def home_view(request):
    context = {'name': 'Akshit Mithaiwala'}
    return render(request, 'index.html', context)


def product_search_view(request):
    try:
        query_params = request.GET.get('q')
        product = Product.objects.filter(title__icontains=query_params[0])
        print(product[0])
    except IndexError:
        raise Http404

    context = {"query": query_params, "product": product[0]}
    return render(request, 'products/search.html', context)


# def product_add_view(request):
#     # print(request.POST)
#     # print(request.GET)
#     product_form = ProductForm(request.POST)
#     # print(product_form.is_valid())
#     if request.method == 'POST':
#         if product_form.is_valid():
#             title_input = product_form.cleaned_data.get('title')
#             Product.objects.create(
#                 title=title_input
#             )
#     return render(request, 'products/add.html')

@staff_member_required
def product_add_view(request):
    product_form = ProductForm(request.POST or None)
    # print(product_form.is_valid())
    if product_form.is_valid():
        data = product_form.cleaned_data
        print(data)
        Product.objects.create(**data)
    return render(request, 'products/add.html', {"product_form": product_form})


def product_details_view(request, productId):
    try:
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist:
        raise Http404  # render html page, with http status code 404
    # return HttpResponse(f"<h1>Hello fellas! {products.title} </h1>")
    # pass object with WITH to header to display with user is login or not!! {% include 'header.html' with user = request.user %}
    return render(request, 'products/details.html', {"product": product})


def products_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {"products": products})


def product_details_view_api(request, productId):
    # products = Product.objects.get(id=1)
    # for product in products:
    #     print(product.id)
    # print(products)
    try:
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist:
        return JsonResponse({"message": 'Not Found'}, status=404)
    return JsonResponse({"title": product.title})
