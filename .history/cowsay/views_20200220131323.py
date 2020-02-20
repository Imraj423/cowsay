import subprocess
from django.shortcuts import render
from .forms import cowform



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


def last_10(request):
    html = 'index.html'

    if request.method == 'POST':
        form = NewTicket(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Cow.objects.create(
                history=data['history']
            )

            

   

    return render(request, html, {'form': form})
