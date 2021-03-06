import xadmin

from common.ModelUtils import get_not_show_properties_extend
from .models import MultiCategory, MultilanguageCategory, CategoryPicture

not_show_in_admin_page_params = ['delete_flag']
not_show_in_admin_page_params_common = get_not_show_properties_extend(not_show_in_admin_page_params)



class MultiCategoryAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["parent", "category_type", "show_order","tenant"]
    list_filter = ["category_type", "tenant"]
    search_fields = ["category_type","parent"]

    show_detail_fields = []



    add_not_show_properties = ['delete_flag']
    not_show_in_admin_page_params_information = get_not_show_properties_extend(add_not_show_properties)
    exclude = not_show_in_admin_page_params_information

    class MultilanguageCategoryInline(object):
        model = MultilanguageCategory
        extra = 1
        exclude = not_show_in_admin_page_params_common
        style = 'tab'

    class CategoryPictureInline(object):
        model = CategoryPicture
        extra = 1
        exclude = not_show_in_admin_page_params_common
        style = 'tab'

    inlines = [MultilanguageCategoryInline,CategoryPictureInline]



class MultilanguageCategoryAdmin(object):
    list_display = ["category", "name", "language_code", "description"]
    list_filter = ["language_code", "name"]
    search_fields = ["name"]
    list_editable = ['name','description']

    show_detail_fields = ["category", "name", "language_code", "description"]
    # 某一个model指向它时，它是以ajax加载的方式来完成的，通过搜索来进行添加某个字段，这样可以避免数据量过大时，把所有数据都加载进来
    relfield_style = 'fk-ajax'
    exclude = not_show_in_admin_page_params_common


class CategoryPictureAdmin(object):
    refresh_times = (1,3, 5,10)

    list_display = ["file", "category"]
    list_filter = ["category"]
    search_fields = ["file", "category"]
    list_editable = []

    show_detail_fields = ["file", "category_picture_type", "category"]
    # 某一个model指向它时，它是以ajax加载的方式来完成的，通过搜索来进行添加某个字段，这样可以避免数据量过大时，把所有数据都加载进来
    relfield_style = 'fk-ajax'
    exclude = not_show_in_admin_page_params_common


xadmin.site.register(MultiCategory, MultiCategoryAdmin)