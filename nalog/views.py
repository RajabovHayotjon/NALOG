from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import QueueForm
from .models import Directors, home_contact


def about_view(request):
    abouts = Directors.objects.all()
    ctx = {
        'abouts': abouts,
    }
    return render(request, 'article/about.html', ctx)


def home_view(request):
    # contact = home_contact.objects.all()
    form = QueueForm()
    if request.method == 'POST':
        form = QueueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    ctx = {
        'form': form,
    }
    return render(request, 'article/index.html', ctx)





