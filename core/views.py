from django.shortcuts import render
from django.contrib import messages
from .forms import MessageForm
from .models import *
import random

# Create your views here.

def index(request):
    # nav = Nav.objects.first()
    hero = Hero.objects.first()
    about = About.objects.first()
    gallery = Showcase.objects.all().order_by('?')
    faq = FAQ.objects.all().order_by('?')[:5]
    cta = CTA.objects.first()
    
    rev_query = Rev.objects.all()
    revs = random.sample(list(rev_query), min(len(rev_query), 3))

    blog = Blog.objects.all().order_by('-id')[:4]
    scocials = Socials.objects.all()
    support = Support.objects.all().order_by('-id')[:6]
    contact = Contacts.objects.all().order_by('id')
    map = Map.objects.first()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            form = MessageForm()  # Clear the form after successful submission
        else:
            messages.error(request, 'There was an error in your form. Please correct it and try again.')
    else:
        form = MessageForm()


    return render(request, 'core/index.html', {
        # 'nav' : nav,
        'hero' : hero,
        'about' : about,
        'gallery' : gallery,
        'faq' : faq,
        'cta' : cta,
        'revs' : revs,
        'blog' : blog,
        'scocials' : scocials,
        'support' : support,
        'form' : form,
        'contact' : contact,
        'map' : map,

    })

# def about(request):

#     return render(request, 'core/about.html')