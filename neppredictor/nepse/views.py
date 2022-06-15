from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.http import Http404
import requests as requests

# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        pass


class LoginView(View):
    def get(self, request):
        return render(request, )

    def post(self, request):
        pass


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        raise Http404


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        raise Http404


class LiveTradeView(View):
    def get(self, request):
        # Calling Microservice
        data = requests.get('http://127.0.0.1:9080/crawl.json?spider_name=daily_prices&start_requests=True')
        info = data.json()
        print(info)
        return render(request, 'livetrade.html', context={'items': info['items']})

class LayoutFile(View):
    def get(self, request):
        return render(request, 'layout.html')
