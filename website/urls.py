from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),    
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    # Detailed Finance Services
   path('services/us-incorporation/', views.incorporation),
path('services/bookkeeping/', views.bookkeeping),
path('services/itin/', views.itin),
path('services/cpa-letter/', views.cpa_letter),
path('services/tax-filing/', views.tax_filing),
path('services/finance-solutions/', views.finance_solutions),
path('services/finance-analysis/', views.finance_analysis),
path('who_we_help', views.who_we_help, name='who_we_help'),
path('index', views.index, name='index'),
path('privacy_policy', views.privacy_policy, name='privacy_policy'),
path('terms', views.terms, name='terms'),   
path('disclaimer', views.disclaimer, name='disclaimer'),
 path('robots.txt', views.robots_txt, name='robots_txt'),


    # Resources
 
    # Trust & Legal
    
  
   
]
