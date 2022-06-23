from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from ifeelapp.script.saavan import JioSaavn

# Initializing Main Class
saavan = JioSaavn()
context = {}

class Home(View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        return redirect('/main')

class Main(View):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.template_name = "index.html"

    def get(self, request, *args, **kwargs):
        global context
        query = kwargs.get("query")
        if query:
            response = [saavan.details(song) for song in saavan.search(query)]
            context = {
                "query": query,
                "database": response
            }
            return render(request, self.template_name, context)

        id = kwargs.get("id")
        lyrics = kwargs.get("lyrics")
        url = self.request.GET.get('url')
        title = self.request.GET.get('title')
        subtitle = self.request.GET.get('subtitle')
        image = self.request.GET.get('image')
        
        if id and lyrics and url:
            url = url.replace(" ","+")
            songUrl = saavan.song(id, url)
            context["songMeta"] = {
                "title": title,
                "subtitle": subtitle,
                "image": image,
                "songUrl": songUrl
            }
            return render(request, self.template_name, context)
        
        query = "new songs"
        response = [saavan.details(song) for song in saavan.search(query)]
        context = {
                "query": query,
                "database": response
            }
        return render(request, self.template_name, context)