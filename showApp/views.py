import pymongo
import pprint
import json
from .forms import ShowForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from bson.json_util import loads, dumps

client = pymongo.MongoClient("mongodb+srv://crigar:crigar123@cluster0.9kt1dbj.mongodb.net/?retryWrites=true&w=majority")
db = client["showDb"]
showsCollection = db["shows"]

@csrf_exempt
def storeAndAnalyze(request):
    showsCollection.delete_many({})
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['data']
    showsByGen = {}
    for schedule in content:
        show = schedule["_embedded"]["show"]
        for gen in show["genres"]:
            if gen in showsByGen:
                showsByGen[gen].append(show)
            else:
                showsByGen[gen] = [show]
        showsCollection.insert_one(show)
    
    return JsonResponse(json.loads(dumps(showsByGen)))