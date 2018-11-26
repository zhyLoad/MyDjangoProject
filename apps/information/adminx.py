import xadmin
from .models import Information, MultilanguageInformation, FileResource,PosterResource


class InformationAdmin(object):
    refresh_times = (1,3, 5,10)
    list_export = ('xls', 'xml', 'json')

    list_display = ["information_type", "information_status", "tenant","audit_reason"]
    list_filter = ["information_type", "information_status"]
    search_fields = ["information_status","information_status"]

    show_detail_fields = []


class MultilanguageInformationAdmin(object):
    list_display = ["information", "name", "language_code", "description"]
    list_filter = ["language_code", "name"]
    search_fields = ["name"]
    list_editable = ['name','description']

    show_detail_fields = ["information", "name", "language_code", "description"]


class FileResourceAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["name", "size","resource_url","information"]
    list_filter = ["name", "resource_url"]
    search_fields = ["name","resource_url"]
    list_editable = []

    show_detail_fields = ["name", "original_name", "size","resource_url","information"]


class PosterResourceAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["name", "size", "resource_url","information"]
    list_filter = ["name", "resource_url"]
    search_fields = ["name", "resource_url"]
    list_editable = []

    show_detail_fields = ["name", "original_name", "size","resource_url","information","horizontal_resoution","vertical_resoution"]



xadmin.site.register(Information, InformationAdmin)
xadmin.site.register(MultilanguageInformation, MultilanguageInformationAdmin)
xadmin.site.register(FileResource, FileResourceAdmin)
xadmin.site.register(PosterResource, PosterResourceAdmin)