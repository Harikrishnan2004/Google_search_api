from django import forms
from django.shortcuts import render
from django.http import HttpResponse
import requests

API_KEY = "AIzaSyCpxvjbaJ9CMD3ZYM4AwUZVtB0mJapTHt4"
SEARCH_ENGINE_ID = "84b42b3fd74ce4397"
url = 'https://www.googleapis.com/customsearch/v1'

class SearchQueryForm(forms.Form):
    query = forms.CharField(label=False)

def home(request):
    return render(request, "google_seo_api/home.html")

def get_links(request):
    links = []
    if request.method == "POST":
        form = SearchQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            print(query)
            params = {
                'q': query,
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID
            }

            response = requests.get(url, params=params)
            results = response.json()['items']

            for item in results:
                links.append(item['link'])

        else:
            return render(request, 'google_seo_api/search_links.html', {
                "form": SearchQueryForm(),
                "links": links
            })
    return render(request, 'google_seo_api/search_links.html', {
        "form": SearchQueryForm(),
        "links": links
    })

def get_images(request):
    images = []
    if request.method == "POST":
        form = SearchQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            print(query)
            params = {
                'q': query,
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID,
                'searchType': 'image'
            }

            response = requests.get(url, params=params)
            results = response.json()['items']

            for item in results:
                images.append(item['link'])

        else:
            return render(request, 'google_seo_api/search_images.html', {
                "form": SearchQueryForm(),
                "images": images
            })
    return render(request, 'google_seo_api/search_images.html', {
        "form": SearchQueryForm(),
        "images": images
    })

def get_pdfs(request):
    pdfs = []
    if request.method == "POST":
        form = SearchQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            print(query)
            params = {
                'q': query,
                'key': API_KEY,
                'cx': SEARCH_ENGINE_ID,
                'fileType': 'pdf'
            }

            response = requests.get(url, params=params)
            results = response.json()['items']

            for item in results:
                pdfs.append(item['link'])

        else:
            return render(request, 'google_seo_api/search_pdfs.html', {
                "form": SearchQueryForm(),
                "pdfs": pdfs
            })
    return render(request, 'google_seo_api/search_pdfs.html', {
        "form": SearchQueryForm(),
        "pdfs": pdfs
    })