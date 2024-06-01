from json_store import views
from django.urls import path

urlpatterns = [
    path("wifi-post",views.WIFICreateAPIView.as_view(),name="wifi-post"),
    path("pywifi-pyscript",views.PyWifiScript.as_view(),name="wifi-script"),
    path("whatsapp_automation_xpath/<str:username>",views.WAXPListAPIView.as_view(),name="whatsapp_automation_xpath"),
    path("whatsapp_automation_script/<str:username>",views.WAScriptListAPIView.as_view(),name="whatsapp_automation_script"),
]