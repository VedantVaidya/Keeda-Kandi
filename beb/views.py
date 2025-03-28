from django.shortcuts import render, redirect
from django.http import HttpResponse
from beb import models


def valentine_template(request):
    return render(request,"index.html")
    return HttpResponse("Reached here")

def birthday(request):
    status = models.MyJSON.objects.get(id=2)
    vid = models.MyJSON.objects.get(id=1)
    on_vid = vid.data["on"]
    off_vid = vid.data["off"]
    if status.data['status']:
        return redirect(on_vid)
    return redirect(off_vid)

def switch_proposal(request):
    status = models.MyJSON.objects.get(id=2)
    if status.data["status"] == True:
        status.data["status"] = False
    else:
        status.data["status"] =True
    status.save()
    return HttpResponse(status.data["status"])