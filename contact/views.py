from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import ContactUs, Practice


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    ctx = {
        'form': form
    }
    return render(request, 'contact/contact.html', ctx)


def practice_areas(request):
    practices = Practice.objects.all()
    ctx = {
        'practices': practices,
    }
    return render(request, 'contact/practice-areas.html', ctx)
