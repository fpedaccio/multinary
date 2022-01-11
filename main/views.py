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
    try:
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
    except:
        definition = "No definition found"
    try:
        example = data[0]["meanings"][0]["definitions"][0]["example"]
    except:
        example = "No example available"
    try:
        phonetic = data[0]["phonetic"]
    except:
        phonetic = "No phonetic available"
    try:
        audio = data[0]["phonetics"][0]["audio"]
    except:
        audio = "No audio available"
    return render(request, 'main/response_en.html', {'definition': definition, 'example': example, "word": word, "phonetic": phonetic,"audio": audio})

def search_es(request):
    word = request.POST["wordInput"]
    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/es/{word}')	
    data = response.json()
    try:
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
    except:
        definition = "No encontramos una definición a esta palabra"
    try:
        example = data[0]["meanings"][0]["definitions"][0]["example"]
    except:
        example = "No hay ejemplo disponible"
    return render(request, 'main/response_es.html', {'definition': definition, 'example': example, "word": word})