from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'home.html',context)