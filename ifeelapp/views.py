from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from ifeelapp.script.saavan import JioSaavn


class Home(View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return redirect('/main')

class Main(View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        if kwargs.get("query"):
            return render(request, template_name=self.template_name)
        return HttpResponse("No Parameter Present")
