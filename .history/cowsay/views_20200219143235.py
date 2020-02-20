from django.shortcuts import render, reverse, HttpResponseRedirect


def index(request):
    context=''
    return render(request, 'index.html', context)
