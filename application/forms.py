import json
from collections import namedtuple

from django import forms
from application import models
from infrastructure.components import methods
from .base import model_base


class ApplicationCategory(forms.ModelForm):
    class Meta:
        model = models.ApplicationCategory
        fields = '__all__'


class ApplicationItem(forms.ModelForm):
    class Meta:
        model = models.ApplicationItem.objects.get(itemID="1")
        fields = '__all__'
        form = model_base.Promissory.from_json(model.content)
        a = form.date
