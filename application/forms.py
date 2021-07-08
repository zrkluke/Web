from django.utils.translation import gettext_lazy as _  # 新增

from django import forms
from application import models
from application.base import model_base


# Django form 可以直接讓前端透過get post做溝通
# 建立每個表單所需要的form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Consumer
        fields = '__all__'
        widgets = {
            'timeStamp': forms.HiddenInput(),
        }
        labels = {
            'LineID': _('LineID'),
            'name': _('全名'),
            'phone': _('手機號碼'),
            'email': _('信箱'),
        }


class PromissoryForm(forms.ModelForm):
    class Meta:
        model = model_base.Promissory
        # exclude = ('orderID',)
        fields = '__all__'
        widgets = {
            'orderID': forms.HiddenInput(),
            'price': forms.HiddenInput(),
        }
        labels = {
            'promissoryAmount': _('本票金額'),
            'promissoryNote': _('本票票號'),
            'nationalID': _('發票人身分證統一編號'),
            'address': _('聲請人地址'),
            'promissoryAddress': _('本票地址'),
            'promissoryDate': _('填寫日期'),
            'promissoryLastDate': _('本票到期日'),
            'promissoryNoticeDate': _('本票提示日'),
            'promissoryCourt': _('發票地管轄法院'),
            'date': _('填寫日期'),
        }
