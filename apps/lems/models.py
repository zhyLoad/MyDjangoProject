from django.db import models
from system_manage.models import Tenant
from common.models import BaseEntry

class Category(BaseEntry):
  """
  目录
  """
  CATEGORY_TYPE = (
      (0,"直播"),(1,"资讯"),(2,"音乐"),(3,"点播"),(4,"餐饮"),(5,"商城")
  )

  parent_id = models.IntegerField(null=False, default=-1,verbose_name=u"租户")
  category_type = models.IntegerField(choices=CATEGORY_TYPE,null=False, blank=True,default=1, verbose_name="目录类型")
  show_order = models.IntegerField(default=9999, null=True,  verbose_name="排序字段")
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name=u"租户")
  delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

  class Meta:
      verbose_name = '目录'
      verbose_name_plural = verbose_name


class CategoryPicture(BaseEntry):
    """
    目录的图片资源
    """
    CATEGORY_PICTURE__TYPE = (
        (0, "图标"), (1, "海报")
    )

    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"目录")
    category_picture_type = models.IntegerField(choices=CATEGORY_PICTURE__TYPE, null=False, blank=True, default=0, verbose_name="目录图片类型")
    size = models.IntegerField(null=True, verbose_name="图片大小")
    resource_url = models.CharField(max_length=4096 ,null=False,default="", verbose_name="图片路径")
    original_name = models.TextField(max_length=100,null=False,default="", verbose_name="原文件名")
    name = models.TextField(max_length=100,null=False,default="", verbose_name="文件名")
    horizontal_resoution = models.IntegerField(null=True, verbose_name="垂直分辨率")
    vertical_resoution = models.IntegerField(null=True, verbose_name="水平分辨率")
    delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

    class Meta:
        verbose_name = "目录图片资源"
        verbose_name_plural = verbose_name


class MultilanguageCategory(BaseEntry):
    """
    目录多语言
    """
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"目录")
    phoneticize = models.CharField(max_length=100,null=True,blank=True,verbose_name="拼音名称")
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name="多语言名称")
    language_code = models.CharField(max_length=50,null=False,default="chi",blank=True,verbose_name="语言编码")
    description = models.TextField(max_length=4096,null=True,verbose_name="描述")
    delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

    class Meta:
        verbose_name = "图文多语言"
        verbose_name_plural = verbose_name