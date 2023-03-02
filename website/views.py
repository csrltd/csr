from django.shortcuts import render, redirect
import os
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from .forms import *
from .models import *
from django.conf import settings


#website
def index(request):
    page_title = 'Home'
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    context = {'form': form, 'page_title':page_title}
    return render(request, 'index.html', context)

def about_us(request):
    page_title = 'About Us'
    context = {'page_title': page_title}
    return render(request, 'about.html', context)

def softwareDev(request):
    page_title = 'Software Development'
    context = {'page_title': page_title}
    return render(request, 'software-dev.html')

def features(request):
    features = Feature.objects.all()
    context = {'features':features}
    return render(request, 'features.html', context)

def thankYou(request):
    return render(request, 'thank-you.html')

def gallery(request):
    return render(request, 'coming-soon.html')

def comingSoon(request):
    return render(request, 'coming-soon.html')


def contact(request):
    page_title = 'Contact'
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    context = {'form': form, 'page_title': page_title}
    return render(request, 'contact.html', context)


def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    page_title = blog.title
    context = {'blog':blog, 'page_title':page_title}
    return render(request, 'coming-soon.html', context)
    
#blog
def blogs(request):
    page_title = 'Blog posts'
    blogs = Blog.objects.filter(status='Published')
    context = {'blogs':blogs, 'page_title': page_title}
    return render(request, 'coming-soon.html', context)

def blogCategories(request):
    categories = Category.objects.all()
    
    return render(request, 'adminDashboard.html')

def blogCategory(request):
    return render(request, 'adminDashboard.html')



#SEO
def sitemap(request):
    template = loader.get_template('sitemaps/sitemap.xml')
    content_type = 'application.xml'
    rendered_template = template.render()

    return HttpResponse(rendered_template, content_type = content_type)


def application(request):
    from django.core.files.storage import default_storage
    from django.core.files.base import ContentFile
    
    page_title = 'Application'
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST,request.FILES)
        
        print('Received')
        if form.is_valid():
            # cv_file = form.cleaned_data['cv']
            # print(cv_file)
            # uploaded_file = request.FILES['cv']
            # print(uploaded_file)
            form.save()
            return redirect('thank-you')
        else:
            return redirect('index')
    context = {'form': form, 'page_title': page_title}
    return render(request,'application.html',context)


def socialMediaPage(request):
    page_title = 'Social Media'

    context = {'page_title': page_title}

    return render(request, 'social-media.html', context)

def taxPreparation(request):
    page_title = 'Tax Preparation'
    page = 'Services'
    title = 'Tax Preparation'
    description = 'An excellent seal of thought went into crafting a proposal for services that adequately meet your accounting needs, and we are confident that you will find precisely what you are looking for in this proposal.'

    context = {'page_title': page_title,'page':page,'title':title,'description':description}

    return render(request, 'taxPreparation.html', context)
