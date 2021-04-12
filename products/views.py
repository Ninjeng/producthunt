from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from operator import attrgetter
from . import forms
from . import models

from django.http import HttpResponse


from accounts.models import Account

# Create your views here.



def home(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    products = sorted(get_product_queryset(query), key=attrgetter('date_updated'), reverse=True)
    context['products'] = products
    return render(request, "products/home.html", context)


def create_product_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    form = forms.CreateProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = forms.CreateProductForm()
    context['form'] = form
    return render(request, 'products/create.html', context)


def detail_product_view(request, slug):
    context = {}
    products = get_object_or_404(models.Product, slug=slug)
    context['products'] = products
    return render(request, 'products/detail.html', context)


def delete_product_view(request, slug=None):
    user = request.user
    post_to_delete = models.Product.objects.get(slug=slug)
    if post_to_delete.author != user:
        return HttpResponse("you are not author")
    post_to_delete.delete()
    return redirect('home')


def edit_product_view(request, slug):
    context = {}
    user = request.user
    product = get_object_or_404(models.Product, slug=slug)
    if product.author != user:
        return HttpResponse("You are not author")
    if request.POST:
        form = forms.UpdateProductForm(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            product = obj

    form = forms.UpdateProductForm(
        initial={
            "product_name": product.product_name,
            "body": product.description,
            "image": product.image,
        }
    )
    context['form'] = form
    return render(request, 'products/edit.html', context)


def get_product_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        product = models.Product.objects.filter(
            Q(product_name__contains=q) |
            Q(description__icontains=q)
        ).distinct()
        for post in product:
            queryset.append(post)
    return list(set(queryset))