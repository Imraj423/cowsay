import subprocess
from .forms import cowform
from .models import Cow
from django.shortcuts import render, reverse, HttpResponseRedirect


def index(request):
    if request.method == "POST":
        form = cowform(request.POST)
        if form.is_valid():
            cow_text = form.cleaned_data['text_input']
            form.save()
            return render(request, 'index.html', {
                'form': cowform(),
                'text': cowsay_helper(cow_text)
            })
            Cow.objects.create(
                history=cow_text
            )
            return HttpResponseRedirect(reverse("history"))
    return render(request, 'index.html', {
        'form': cowform()
    })


def cowsay_helper(text):
    cmd = subprocess.Popen(
        ['cowsay', text],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    out, err = cmd.communicate()
    if err:
        raise err
    else:
        return out.decode().split("\n")


# def last10(request):
#     item = history.objects.all()
#     return render(request, 'history.html', {'data': item})
