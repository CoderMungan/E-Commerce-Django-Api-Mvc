from django.shortcuts import render
from django.http import JsonResponse
from siteApp.models import *

# Create your views here.

def sepete_ekle(request,urunId):
    context = {}

    sepet = Sepet.objects.filter(urun__id = urunId).first()
    if sepet is None:
        context['error'] = "Böyle bir ürün bulunmamaktadır"
        return JsonResponse(context)
    sepet.sepeteAtilma = True
    sepet.save()


    data = {
        "name": sepet.urun.urunBaslik,
        "adet": sepet.adet,
    }

    context['data'] = data

    return JsonResponse(context)


def sepet_adet_ekle(request,urunId):

    context = {}

    sepet = Sepet.objects.filter(urun__id = urunId).first()
    if sepet is None:
        context['error'] = "Böyle bir ürün bulunmamaktadır"
        return JsonResponse(context)
    sepet.adet += 1
    sepet.save()


    data = {
        "name": sepet.urun.urunBaslik,
        "adet": sepet.adet,
    }

    context['data'] = data

    return JsonResponse(context)