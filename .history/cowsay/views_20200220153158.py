import subprocess
from .forms import cowform
from cowsay.models import Cow
from django.shortcuts import render


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
    return render(request, 'index.html', {
        'form': cowform()
    })


def cowsay_helper(text):
    context = {
        'items': cowsay.models.Cow.objects.filter(name='cow'),
        'types': cowsay_models.Cow_Type.objects.all()
    }
    cmd = subprocess.Popen(
        ['cowsay', '-f', Cow_Type, text],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    out, err = cmd.communicate()
    if err:
        raise err
    else:
        return out.decode().split("\n")


def last10(request):
    item = Cow.objects.all().order_by("-time")
    return render(request, 'history.html', {'data': item[:10]})
