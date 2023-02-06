from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.conf import settings
# Create your views here.

def index(request):
    page_title = 'Home'
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    context = {'form': form, 'page_title':page_title}

    if settings.COMMING_SOON:
        return render(request, 'coming-soon.html')
    return render(request, 'index.html', context)

def blog(request, slug):
    page_title = 'Blog posts'
    blog = Blog.objects.get(slug=slug)
    context = {'blog':blog}
    return render(request, 'single-blog.html', context)

def blogs(request):
    page_title = 'Blog posts'
    blogs = Blog.objects.filter(status='Published')
    context = {'blogs':blogs, 'page_title': page_title}
    return render(request, 'blog.html', context)

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

def coming_soon(request):
    return render(request, 'coming-soon.html')