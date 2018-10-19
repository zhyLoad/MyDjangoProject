import xadmin
from .models import Tenant,Manager,Organization


class TenantAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["name", "phone", "email","status"]
    list_filter = ["name", "status"]
    search_fields = ["name","status"]

    show_detail_fields = []



class ManagerAdmin(object):
    list_display = ["name", "phone", "email", "tenant"]
    list_filter = ["name", "tenant"]
    search_fields = ["name"]
    list_editable = ['name']

    show_detail_fields = []




class OrganizationAdmin(object):
    refresh_times = (1,3, 5,10)
    list_export = ('xls', 'xml', 'json')

    list_display = ["name", "phone", "tenant"]
    list_filter = ["name", "tenant"]
    search_fields = ["name"]
    list_editable = ['name']

    show_detail_fields = []





xadmin.site.register(Tenant, TenantAdmin)
xadmin.site.register(Manager, ManagerAdmin)
xadmin.site.register(Organization, OrganizationAdmin)