from django.shortcuts import render
import requests
from .models import search_data
from django.db.models import Count
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
        searched = search_data(word=word)
        searched.save()
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
        searched = search_data(word=word)
        searched.save()
    except:
        definition = "No encontramos una definición a esta palabra"
    try:
        example = data[0]["meanings"][0]["definitions"][0]["example"]
    except:
        example = "No hay ejemplo disponible"
    return render(request, 'main/response_es.html', {'definition': definition, 'example': example, "word": word})

def stats(request):
    most_common = list(search_data.objects.values("word").annotate(count=Count('word')).order_by("-count")[:5])
    total_obj = search_data.objects.count()
    top_1 = most_common[0]["word"]
    top_2 = most_common[1]["word"]
    top_3 = most_common[2]["word"]
    top_4 = most_common[3]["word"]
    top_5 = most_common[4]["word"]
    top_1_count = most_common[0]["count"]
    top_2_count = most_common[1]["count"]
    top_3_count = most_common[2]["count"]
    top_4_count = most_common[3]["count"]
    top_5_count = most_common[4]["count"]
    total = top_1_count + top_2_count + top_3_count + top_4_count + top_5_count
    relation_1 = top_1_count / total
    relation_2 = top_2_count / total
    relation_3 = top_3_count / total
    relation_4 = top_4_count / total
    relation_5 = top_5_count / total

    return render(request, 'main/stats.html', {"total_obj":total_obj,"relation_1": relation_1, "relation_2": relation_2, "relation_3": relation_3,"relation_4": relation_4, "relation_5": relation_5,"total":total,"top_1": top_1, "top_2": top_2, "top_3": top_3, "top_4": top_4, "top_5": top_5, "top_1_count": top_1_count, "top_2_count": top_2_count, "top_3_count": top_3_count, "top_4_count": top_4_count, "top_5_count": top_5_count})
   
         
