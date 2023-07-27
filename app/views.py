from django.shortcuts import render

# Create your views here.


def data_render(request):
    d = {'name':'Anjali', 'age':'22'}
    return render(request,'data_render.html', context = d)