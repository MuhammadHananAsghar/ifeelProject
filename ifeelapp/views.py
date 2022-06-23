from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class Home(View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

