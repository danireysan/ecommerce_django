from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Company
# Create your views here.


class CompanyView(View):

    def get(self, request):
        companies = Company.objects.all()
        if len(companies) > 0:
            datos = {'message': "Sucess", 'companies': companies}
        else:
            datos = {'message': 'Companies not found'}
        return JsonResponse(datos)    

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
