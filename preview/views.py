from django.shortcuts import render, get_object_or_404

import application.forms
from application import models
from application.base import model_base
from .forms import ApplicationForm


# Create your views here.
def previewApplication(request):
    if request.method == "GET":
        request.GET = request.GET.copy()
        orderID = request.GET.__getitem__('orderID')
        content = models.Order.objects.get(orderID=orderID).content
        instance = model_base.Promissory.from_json(content)
        form = ApplicationForm(instance=instance)
        context = {
            'form': form,
        }
        return render(request, './application/preview/../templates/application/preview.html', context)
