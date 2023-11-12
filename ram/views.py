from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
import psutil


def ram_data(request):
    ram_info = psutil.virtual_memory()
    print(ram_info)
    data = {
        'avaliable': ram_info[1] / (1024 * 1024),
        'date': date.today(),
    }
    return JsonResponse(data)
