from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):
    @staticmethod
    def get(request):
        context = {}
        return render(request, 'index.html', context)

class ProfileView(View):
    @staticmethod
    def get(request):
        context = {}
        return render(request, 'profile.html', context)
