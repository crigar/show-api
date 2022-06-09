from django.shortcuts import render
from pymongo import MongoClient

# Create your views here.
client = pymongo.MongoClient("mongodb+srv://crigar:123456789@cluster0.9kt1dbj.mongodb.net/?retryWrites=true&w=majority")
db = client.show-db