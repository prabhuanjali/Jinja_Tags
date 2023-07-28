from django.shortcuts import render

# Create your views here.


def data_render(request):
    d = {'name':'Anjali', 'age':22}
    return render(request,'data_render.html', context = d)

def if_else(request):
    d = {'a': 10, 'b': 25}
    return render(request,'if_else.html', context = d)

def if_elif_else(request):
    d = {'a': 10, 'b': 25, 'c': 190}
    return render(request, 'if_elif_else.html', context = d)