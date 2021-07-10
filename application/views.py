# -*-coding:utf-8 -*-
import datetime
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.views import View
from django.views.generic import ListView

from application import forms
from application import models
from application.base import model_base
from infrastructure.components.methods import convert_to_json


def checkOrderID(date, orderID):
    if date != datetime.date.today().strftime('%Y%m%d'):
        date = datetime.date.today().strftime('%Y%m%d')
        return date + '{num:0{width}}'.format(num=orderID, width=4)
    else:
        try:
            order = date + '{num:0{width}}'.format(num=orderID, width=4)
            temp = model_base.Promissory.objects.get(orderID=order)
            while temp is not None:
                orderID += 1
                order = date + '{num:0{width}}'.format(num=orderID, width=4)
                temp = model_base.Promissory.objects.get(orderID=order)
        except:
            return date + '{num:0{width}}'.format(num=orderID, width=4)
    return date + '{num:0{width}}'.format(num=orderID, width=4)


def CreateOrder(applicationForm, LineID, orderID):
    consumer = models.Consumer.objects.get(LineID=LineID)
    model = models.ApplicationItem.objects.get(itemID="1")
    orderModel = models.Order(
        orderID=orderID,
        orderStatus="Created",
        price=applicationForm.cleaned_data['price'],
        content=convert_to_json(model_to_dict(applicationForm.instance)),
        consumer=consumer,
        timeStamp=str(datetime.datetime.today()),
    )
    orderModel.save()


def createApplication(request):
    if request.method == 'GET':
        content = models.ApplicationItem.objects.get(itemID='1').content
        instance = model_base.Promissory.from_json(content)
        form = forms.PromissoryForm(instance=instance)
        form2 = forms.CustomerForm
        context = {
            'form': form,
            'form2': form2
        }
        return render(request, 'application.html', context)
    else:
        orderID = checkOrderID(datetime.date.today().strftime('%Y%m%d'), 1)
        request.POST = request.POST.copy()
        request.POST.__setitem__('orderID', orderID)
        request.POST.__setitem__('timeStamp', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        form = forms.PromissoryForm(request.POST)
        form2 = forms.CustomerForm(request.POST)
        if form.is_valid():
            form.save()

        LineID = request.POST['LineID']
        if LineID is not None:
            if form2.is_valid():
                form2.save()

        CreateOrder(form, LineID, orderID)
        context = {
            'orderID': orderID,
        }
    return render(request, './application/preview.html', context)



