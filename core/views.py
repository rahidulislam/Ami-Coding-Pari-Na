from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import KhojForm
from .models import KhojTheSearch
from django.contrib import messages
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'core/index.html')


class KhojView(View):
    template_name = 'core/khoj.html'
    def get(self, request):
        form = KhojForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = KhojForm(request.POST)
        if form.is_valid():
            input_value = form.cleaned_data.get('input_value')
            search_value = form.cleaned_data.get('search_value')
            value_list = [ int(i) for i in input_value.split(',')]
            sort_value_list = sorted(value_list, reverse=True)
            
            khoj = KhojTheSearch()
            khoj.user = request.user
            khoj.input_value = str(sort_value_list)
            khoj.save()
            
            if search_value in sort_value_list:
                print(True)
                messages.success(request, '{0} is avaiable in this list {1}'.format(search_value, sort_value_list))
            else:
                print(False)
                messages.warning(request, 'Sorry! {0} is not avaiable in this list {1}'.format(search_value, sort_value_list))
        return render(request, self.template_name, {'form': form})