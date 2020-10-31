from django.shortcuts import render
from django.views.generic import TemplateView
from forms import flat_attributes
from .predictor import show_data

class homepage(TemplateView):
    template_name = 'Home/home.html'

    def get(self, request):
        form = flat_attributes()
        return render(request, 'Home/home.html', {'form':form})

    def post(self,request):
        form = flat_attributes(request.POST)
        if form.is_valid():
            example = show_data(request.POST)
            return render(request,'Home/home.html',{'form':form, 'example':example})
        else:
            return render(request, 'Home/home.html', {'form':form})

