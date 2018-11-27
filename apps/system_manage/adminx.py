import xadmin
from .models import Tenant,Manager,Organization
from common.ModelUtils import get_not_show_properties_extend


not_show_in_admin_page_params = ['delete_flag']
not_show_in_admin_page_params_common = get_not_show_properties_extend(not_show_in_admin_page_params)


class TenantAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["name", "phone", "email","status"]
    list_filter = ["name", "status"]
    search_fields = ["name","status"]

    show_detail_fields = []
    exclude = get_not_show_properties_extend(['delete_flag','status'])



class ManagerAdmin(object):
    list_display = ["name", "phone", "email", "tenant"]
    list_filter = ["name", "tenant"]
    search_fields = ["name"]
    list_editable = ['name']

    show_detail_fields = []
    exclude = not_show_in_admin_page_params_common




class OrganizationAdmin(object):
    refresh_times = (1,3, 5,10)
    list_export = ('xls', 'xml', 'json')

    list_display = ["name", "phone", "tenant"]
    list_filter = ["name", "tenant"]
    search_fields = ["name"]
    list_editable = ['name']

    show_detail_fields = []
    exclude = not_show_in_admin_page_params_common





xadmin.site.register(Tenant, TenantAdmin)
xadmin.site.register(Manager, ManagerAdmin)
xadmin.site.register(Organization, OrganizationAdmin)