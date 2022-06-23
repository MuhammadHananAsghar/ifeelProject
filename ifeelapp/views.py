from django.http import HttpResponse, JsonResponse
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
        query = kwargs.get("query")
        if query:
            response = [saavan.details(song) for song in saavan.search(query)]
            context = {
                "query": query,
                "database": response
            }
            return render(request, self.template_name, context)
        
        query = "new songs"
        response = [saavan.details(song) for song in saavan.search(query)]
        context = {
                "query": query,
                "database": response
            }
        return render(request, self.template_name, context)

class Song(View):
    def post(self, request, *args, **kwargs):
        lyrics_id = request.POST['data[lyrics_id]']
        subtitle = request.POST['data[subtitle]']
        id = request.POST['data[id]']
        enc_url = request.POST['data[enc_url]']
        title = request.POST['data[title]']
        image = request.POST['data[image]']
        songUrl = saavan.song(id, enc_url)
        database = {
            "image": image,
            "title": title,
            "subtitle": subtitle,
            "songurl": songUrl
        }
        return JsonResponse(database)

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is not GET request route.")

class Download(View):
    def post(self, request, *args, **kwargs):
        id = request.POST['data[id]']
        enc_url = request.POST['data[enc_url]']
        songUrl = saavan.song(id, enc_url)
        database = {
            "songurl": songUrl
        }
        return JsonResponse(database)

    def get(self, request, *args, **kwargs):
        return HttpResponse("This is not GET request route.")