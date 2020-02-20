from django.shortcuts import render, reverse, HttpResponseRedirect


def index(request):

    return render(request, 'index.html')
