# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.views import View
from business.forms import compare, equal
from business.models import product

# Create your views here.


'''class check(View):
	def valid(request):'''


def signout(request):
    logout(request)
    return render(request, "frontpage.html")


def valid(request):
    if request.method == "POST":
        form = compare(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data saved successfully")
        else:
            content = {'form': form}
            return render(request, "frontpage.html", content)

    else:
        form = compare()
        return render(request, "frontpage.html", {'form': form})


def verify(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        if user.want_to == 'sell':
            return render(request, "seller.html")
        elif user.want_to == 'buy':
            return render(request, "customer.html")
        else:
            return HttpResponse("not a valid user")

    else:
        return HttpResponse("Check something is wrong")


def data(request):
    full1 = product.objects.all()
    full = serializers.serialize('json', full1)
    return render(request, "customer.html", {'full': full})


def sell(request):
    if request.method == "POST":
        form = equal(request.POST)
        if form.is_valid():
            form.save()
            l = "Product Added Successfully"
            return render(request, "seller.html", {'l': l})
        else:
            return render(request, "seller.html", {'form': form})

    else:
        return HttpResponse("Form is not okkk")
