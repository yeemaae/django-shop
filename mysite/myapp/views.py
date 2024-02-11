from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required


def index(request):
    items = Product.objects.all()
    context = {
        "items": items
    }
    return render(request, "myapp/index.html", context=context)


def indexItem(request, id):
    item = Product.objects.get(id=id)
    context = {
        "item": item
    }
    return render(request, "myapp/detail.html", context=context)


@login_required
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        seller = request.user
        item = Product(name=name, price=price, description=description, image=image, seller=seller)
        item.save()

    return render(request, "myapp/additem.html")


def update_item(request, id):
    item = Product.objects.get(id=id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/myapp/")
    context = {
        "item": item
    }
    return render(request, "myapp/updateitem.html", context=context)


def delete_item(request, id):
    item = Product.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("/myapp/")
    context = {
        "item": item
    }
    return render(request, "myapp/deleteitem.html", context=context)


