from django.contrib import admin
from json_store.models import WifiJson, WAXpathJson, WAScriptJson
from import_export.admin import ImportExportModelAdmin


class WifiJsonAdmin(ImportExportModelAdmin):
    list_display = ("name", "data")
    search_fields = ("name",)
    ordering = ("name",)


admin.site.register(WifiJson, WifiJsonAdmin)
admin.site.register(WAXpathJson, admin.ModelAdmin)
admin.site.register(WAScriptJson, admin.ModelAdmin)
