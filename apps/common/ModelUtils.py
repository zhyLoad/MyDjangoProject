from .ModelConstant import common_not_show_in_admin_page_properties


def get_not_show_properties_extend(params_list):
    """
    在现有的不展示字段元组中拼接几个其他的属性，用于每个模块定制化配置哪些字段不用在Admin界面上显示
    :param params_list:
    :return:
    """
    default_list = list(common_not_show_in_admin_page_properties)
    default_list.extend(params_list)
    return tuple(default_list)