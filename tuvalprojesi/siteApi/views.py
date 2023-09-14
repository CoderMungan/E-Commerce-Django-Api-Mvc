from django.shortcuts import render,redirect
from django.http import JsonResponse
from siteApp.models import *

# Create your views here.

def sepete_ekle(request,urunId):
    context = {}

    urun = Urun.objects.filter(id = urunId).first()

    if urun is None:
        context['error'] = "Böyle bir ürün bulunmamaktadır"
    else:
        Sepet.objects.create(urun = urun, user = request.user, sepeteAtilma = True, adet = 1)
        context['message'] = "Sepete Eklendi"
        return redirect('urundetay', urunId)

    return JsonResponse(context)


def sepet_adet_ekle(request,urunId):

    context = {}

    sepet = Sepet.objects.filter(urun__id = urunId).first()

    if sepet:
        sepet.adet += 1
        sepet.save();
        context['message'] = "Adet Eklendi"
        return redirect('urundetay',urunId)

    return JsonResponse(context)

def sepet_adet_cikar(request,urunId):

    sepet = Sepet.objects.filter(urun__id = urunId).first()

    if sepet and sepet.adet > 1:
        sepet.adet -= 1
        sepet.save();
        return redirect('urundetay',urunId)
    else:
        return redirect('urundetay', urunId)
    

def sepetten_kaldir(request,urunId):

    context = {}
    sepet = Sepet.objects.filter(urun__id = urunId).first()
    if sepet:
        sepet.delete()
        context['message'] = "Sepetten Kaldırıldı"
        return redirect('urundetay', urunId)
    
    return JsonResponse(context)

