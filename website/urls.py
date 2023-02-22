from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('about/',about_us,name='about'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('blogs/', blogs, name='blogs'),
    path('blog/<slug:slug>', blog, name='blog'),
    path('features', features, name='features'),
    path('thank-you', thankYou, name='thank-you'),
    path('book-keeping-and-outsourcing-of-staff', service1, name='book-keeping-and-outsourcing-of-staff'),
    path('customer-support', service2, name='customer-support'),
    path('data-entry', service3, name='data-entry'),
    path('payroll-management-and-funding', service4, name='payroll-management-and-funding'),
    path('non-deposit-taking-micorfinance', service5, name='non-deposit-taking-micorfinance'),
    path('financial-analysis-and-calculations-related-services', service6, name='financial-analysis-and-calculations-related-services'),

    path('sitemap', sitemap, name='sitemap'),

    # Added path to category
    path('categories',blogCategories, name='categories'),
    path('category/<slug:slug>', blogCategory, name='category'),
    path('coming-soon', comingSoon ,name='coming-soon')
]