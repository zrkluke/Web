from django.shortcuts import render
from django.views import View
from application import forms


class ApplicationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "application.html")


