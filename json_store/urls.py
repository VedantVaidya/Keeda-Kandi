from json_store import views
from django.urls import path

urlpatterns = [
    path("wifi-post",views.WIFICreateAPIView.as_view(),name="wifi-post"),
    path("pywifi-pyscript",views.PyWifiScript.as_view(),name="wifi-script")
]