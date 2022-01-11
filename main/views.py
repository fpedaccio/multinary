from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def dictionary(request, code):
    if code == "es":
        return render(request, 'main/search_es.html', {'code': code})
    else:
        return render(request, 'main/search_en.html', {'code': code})


def search_en(request):
    word = request.POST["wordInput"]
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')	
    data = response.json()
    definition = data[0]["meanings"][0]["definitions"][0]["definition"]
    example = data[0]["meanings"][0]["definitions"][0]["example"]
    phonetic = data[0]["phonetic"]
    audio = data[0]["phonetics"][0]["audio"]
    return render(request, 'main/response_en.html', {'definition': definition, 'example': example, "word": word, "phonetic": phonetic,"audio": audio})

def search_es(request):
    word = request.POST["wordInput"]
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/es/{word}')	
    data = response.json()
    definition = data[0]["meanings"][0]["definitions"][0]["definition"]
    example = data[0]["meanings"][0]["definitions"][0]["example"]

    return render(request, 'main/response_es.html', {'definition': definition, 'example': example, "word": word})