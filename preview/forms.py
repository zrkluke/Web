from django import forms
from django.utils.translation import gettext_lazy as _
from application.base import model_base


class ApplicationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['field'].widget.attrs['readonly'] = True

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
