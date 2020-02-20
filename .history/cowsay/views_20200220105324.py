from django.shortcuts import render


def index(request):
    if request.method == "POST":
        form = CowEchoForm(request.POST)
        if form.is_valid():
            cow_text = form.cleaned_data['text']
            form.save()
            return render(request, 'index.html', {
                'form': CowEchoForm(),
                'text': cowsay_helper(cow_text)
            })
    return render(request, 'index.html', {
        'form': CowEchoForm()
    })
