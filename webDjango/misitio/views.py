from django.shortcuts import render

# Create your views here.

def clientes_list(request):
    return render(request, 'misitio/clientes_list.html', {})