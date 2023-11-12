from django.shortcuts import render

def doc(request):
    return render(request, 'docs/swagger-ui.html')