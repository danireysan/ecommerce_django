from django.urls import path
from .views import CompanyView
urlpatters=[
    path('companies/', CompanyView.as_view(), name='companies_list')
]