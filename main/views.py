from django.shortcuts import render
from django.views import View

from .models import Main, Services, About, Testimonial


class MainView(View):
    def get(self, request):
        main = Main.objects.all()
        return render(request, "index.html", {"index": main})


class ServicesView(View):
    def get(self, request):
        ser = Services.objects.all()
        return render(request, "service.html", {"service": ser})


class AboutView(View):
    def get(self, request):
        ser = About.objects.all()
        return render(request, "about.html", {"about": ser})
