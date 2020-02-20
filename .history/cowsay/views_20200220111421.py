import subprocess
from django.shortcuts import render


def index(request):
    if request.method == "POST":
        form = cowform(request.POST)
        if form.is_valid():
            cow_text = form.cleaned_data['text']
            form.save()
            return render(request, 'index.html', {
                'form': cowform(),
                'text': cowsay_helper(cow_text)
            })
    return render(request, 'index.html', {
        'form': CowEchoForm()
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
