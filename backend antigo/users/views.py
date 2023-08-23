from django.shortcuts import render
from django.http import HttpResponse


def user(request):
    return HttpResponse('Página Geral Usuario')


def user_detail(request, id):
    return HttpResponse(id)

def user_name(request, nome):
    return HttpResponse(f' Olá {nome}')