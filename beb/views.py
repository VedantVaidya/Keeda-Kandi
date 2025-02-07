from django.shortcuts import render
from django.http import HttpResponse


def valentine_template(request):
    return render(request,"index.html")
    return HttpResponse("Reached here")