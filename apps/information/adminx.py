import xadmin

from common.ModelUtils import get_not_show_properties_extend
from .models import Information, MultilanguageInformation, FileResource,PosterResource

not_show_in_admin_page_params = ['delete_flag']
not_show_in_admin_page_params_common = get_not_show_properties_extend(not_show_in_admin_page_params)



class MultilanguageInformationInline(object):
    model = MultilanguageInformation
    extra = 1
    exclude = not_show_in_admin_page_params_common


class FileResourceInline(object):
    model = FileResource
    extra = 1
    exclude = not_show_in_admin_page_params_common


class PosterResourceInline(object):
    model = PosterResource
    extra = 1
    exclude = not_show_in_admin_page_params_common




class InformationAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["information_type", "information_status", "tenant","audit_reason"]
    list_filter = ["information_type", "information_status"]
    search_fields = ["information_status","information_status"]

    show_detail_fields = []

    inlines = [MultilanguageInformationInline,FileResourceInline,PosterResourceInline]

    add_not_show_properties = ['delete_flag','audit_reason','information_status']
    not_show_in_admin_page_params_information = get_not_show_properties_extend(add_not_show_properties)
    exclude = not_show_in_admin_page_params_information




class MultilanguageInformationAdmin(object):
    list_display = ["information", "name", "language_code", "description"]
    list_filter = ["language_code", "name"]
    search_fields = ["name"]
    list_editable = ['name','description']

    show_detail_fields = ["information", "name", "language_code", "description"]
    # 某一个model指向它时，它是以ajax加载的方式来完成的，通过搜索来进行添加某个字段，这样可以避免数据量过大时，把所有数据都加载进来
    relfield_style = 'fk-ajax'
    exclude = not_show_in_admin_page_params_common



class FileResourceAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["name", "size","resource_url","information"]
    list_filter = ["name", "resource_url"]
    search_fields = ["name","resource_url"]
    list_editable = []

    show_detail_fields = ["name", "original_name", "size","resource_url","information"]
    # 某一个model指向它时，它是以ajax加载的方式来完成的，通过搜索来进行添加某个字段，这样可以避免数据量过大时，把所有数据都加载进来
    relfield_style = 'fk-ajax'
    exclude = not_show_in_admin_page_params_common


class PosterResourceAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["name", "size", "resource_url","information"]
    list_filter = ["name", "resource_url"]
    search_fields = ["name", "resource_url"]
    list_editable = []

    show_detail_fields = ["name", "original_name", "size","resource_url","information","horizontal_resoution","vertical_resoution"]
    # 某一个model指向它时，它是以ajax加载的方式来完成的，通过搜索来进行添加某个字段，这样可以避免数据量过大时，把所有数据都加载进来
    relfield_style = 'fk-ajax'
    exclude = not_show_in_admin_page_params_common


xadmin.site.register(Information, InformationAdmin)
xadmin.site.register(MultilanguageInformation, MultilanguageInformationAdmin)
xadmin.site.register(FileResource, FileResourceAdmin)
xadmin.site.register(PosterResource, PosterResourceAdmin)