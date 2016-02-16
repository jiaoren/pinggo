# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *


def main(request):
    furnitures = Furniture.objects.all()
    for i in range(0,len(furnitures)):
        furnitures[i].furnitureImage = str(furnitures[i].furnitureImage).split('/')[-1]
    rc = RequestContext(request, {'furnitures':furnitures},)
    return render_to_response('index.html', context_instance=rc)

def about(request):
    rc = RequestContext(request, {'prob':'1'},)
    return render_to_response('about.html', context_instance=rc)

def showDetail(request,furnitureID):
    furniture = Furniture.objects.get(id=furnitureID)
    furniture.furnitureImage = str(furniture.furnitureImage).split('/')[-1]
    rc = RequestContext(request, {'furniture':furniture},)
    return render_to_response('overlay.html', context_instance=rc)
    #return HttpResponse(furniture.furnitureImage)
    
