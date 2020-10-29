from django.shortcuts import render
from django.views.generic import TemplateView
from forms import flat_attributes

class homepage(TemplateView):
    template_name = 'Home/home.html'

    def get(self, request):
        form = flat_attributes()
        return render(request, 'Home/home.html', {'form':form})

