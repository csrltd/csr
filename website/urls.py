from django.urls import path
from .views import *
urlpatterns = [
    #Website
    path('', index, name='index'),
    path('about/',about_us,name='about'),
    path('software-dev/',softwareDev,name='software-dev'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('features', features, name='features'),
    path('thank-you', thankYou, name='thank-you'),
    path('coming-soon', comingSoon ,name='coming-soon'),
    path('social-media',socialMediaPage, name='social-media'),
    path("tax-preparation",taxPreparation, name="tax-preparation"),
    path("accounting-book-keeping", accountingBookKeeping, name="accounting-book-keeping"),
    path("micro-finance", microFinance, name='micro-finance'),
    path('controller-services', controllerServices, name='controller-services'),
    path('financial-consulting',financialConsulting,name='financial-consulting'),

    #Blog
    path('blogs/', blogs, name='blogs'),
    path('blog/<slug:slug>', blog, name='blog'),
    path('categories',blogCategories, name='categories'),
    path('category/<slug:slug>', blogCategory, name='category'),
    path('application', application, name='application'),


    #SEO
    path('sitemap', sitemap, name='sitemap'),
]