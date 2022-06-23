from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from ifeelapp.script.saavan import JioSaavn

# Initializing Main Class
saavan = JioSaavn()

class Home(View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return redirect('/main')

class Main(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        query = kwargs.get("query")
        if not query:
            query = "new songs"
        response = [saavan.details(song) for song in saavan.search(query)]
        context = {
            "query": query,
            "database": response
        }
        return render(request, self.template_name, context)
