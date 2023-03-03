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

def financeAccounting(request):
    page_title = 'Accounting and finance services'
    context = {'page_title': page_title}
    return render(request, 'finance-acc.html', context)

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

def accountingBookKeeping(request):

    return render(request, 'accounting-book-keeping.html')


def accountingBookKeeping(request):
    page_title = 'Accounting and Book Keeping'
    page = 'Services'
    title = 'Accounting and book keeping services'
    description = 'An excellent seal of thought went into crafting a proposal for services that adequately meet your accounting needs, and we are confident that you will find precisely what you are looking for in this proposal.'

    context = {'page_title': page_title,'page':page,'title':title,'description':description}


    return render(request, 'accounting-book-keeping.html', context)
def microFinance(request):
    page_title = 'Non Deposit Microfinance'
    page = 'Services'
    title = 'Non-deposit-Microfinance'
    description = 'CSR aims to be part of the non-deposit-taking microfinance institutions offering custom-made working capital solutions to small and medium businesses.'

    context = {'page_title': page_title,'page':page,'title':title,'description':description}

    return render(request, 'non-deposit-microfinance.html', context)

def controllerServices(request):
    page_title = 'Controller Services'
    page = 'Services'
    title = 'Controller services'
    description = 'On or after supervision of accounting and bookkeeping processes to examining strategic goals to assisting make sure compliance with established budgets and growth goals, controllers are the influence that operate perfect financial health.'

    context = {'page_title': page_title,'page':page,'title':title,'description':description}

    return render(request, 'controller-services.html', context)

def financialConsulting(request):
    page_title = 'Financial Consulting'
    page = 'Services'
    title = 'Financial Consulting services'
    description = 'Our financial consulting service are designed to provide you with expert analysis and advice regarding your company’s strategic decisions.'

    context = {'page_title': page_title,'page':page,'title':title,'description':description}

    return render(request, 'financial.html', context)