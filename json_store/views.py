from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from json_store.models import WifiJson
from json_store.serializers import WifiJsonSerializer
from django.http import HttpResponse

class WIFICreateAPIView(CreateAPIView):
    queryset = WifiJson.objects.all()
    serializer_class = WifiJsonSerializer
    
    def create(self, request, *args, **kwargs):
        obj_list=[]
        for key,value in request.data.items():
            if key:
                obj=WifiJson()
                obj.name = key
                obj.data = value
                obj_list.append(obj)
        WifiJson.objects.bulk_create(obj_list)
        return HttpResponse("Hi")
