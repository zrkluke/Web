from django.shortcuts import render, get_object_or_404


# Create your views here.
def previewApplication(request):
    if request.method == "GET":
        request.GET = request.GET.copy()
        form = get_object_or_404(forms.PromissoryForm)
        orderForm = forms.O