from django.shortcuts import render, redirect
import os
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse
from .forms import *
from .models import *
from django.conf import settings

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

def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    page_title = blog.title
    context = {'blog':blog, 'page_title':page_title}
    return render(request, 'singleBlog.html', context)
    

def blogs(request):
    page_title = 'Blog posts'
    blogs = Blog.objects.filter(status='Published')
    context = {'blogs':blogs, 'page_title': page_title}
    return render(request, 'blog.html', context)

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

def features(request):
    features = Feature.objects.all()
    context = {'features':features}
    return render(request, 'features.html', context)

def thankYou(request):
    return render(request, 'thank-you.html')

def service1(request):
    return render(request, 'book-keeping-and-outsourcing-of-staff.html')

def service2(request):
    return render(request, 'customer-support.html')

def service3(request):
    return render(request, 'data-entry.html')

def service4(request):
    return render (request, 'payroll-management-and-funding.html')

def service5(request):
    return render(request, 'non-deposit-taking-micorfinance.html')

def service6(request):
    return render(request, 'financial-analysis-and-calculations-related-services.html')

def about_us(request):
    page_title = 'About Us'
    context = {'page_title': page_title}
    return render(request, 'about.html', context)

def gallery(request):
    return render(request, 'coming-soon.html')

def thankYou(request):
    return render(request, 'thank-you.html')

def blogCategories(request):
    categories = Category.objects.all()
    
    return render(request, 'adminDashboard.html')

def blogCategory(request):
    return render(request, 'adminDashboard.html')

def comingSoon(request):
    return render(request, 'coming-soon.html')



#SEO
def sitemap(request):
    template = loader.get_template('sitemaps/sitemap.xml')
    content_type = 'application.xml'
    rendered_template = template.render()

    return HttpResponse(rendered_template, content_type = content_type)


def application(request):
    
    page_title = 'Application'
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        print('Received')
        if form.is_valid():
            print('valid')
            form.save()
            print('saved')
            return redirect('thank-you')
        else:
            return redirect('index')
    context = {'form': form, 'page_title': page_title}
    return render(request,'application.html',context)