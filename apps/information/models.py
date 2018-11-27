from django.db import models

from system_manage.models import Tenant
from common.models import BaseEntry


class Information(BaseEntry):
  """
  图文信息类
  """
  INFORMATION_TYPE = (
      (0,"新闻"),(1,"图片"),(2,"文档")
  )
  INFORMATION_STATUS = (
      (0,"待审核"),(1,"审核中"),(2,"审核通过"),(3,"审核不通过"),(4,"已发布")
  )
  information_type = models.IntegerField(choices=INFORMATION_TYPE,null=False, blank=True,default=1, verbose_name="图文类型")
  information_status = models.IntegerField(choices=INFORMATION_STATUS,null=False, blank=True,default=0, verbose_name="图文状态")
  tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name=u"租户")
  audit_reason = models.CharField(max_length=2048, null=True, blank=True, verbose_name="审核原因")
  delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

  class Meta:
      verbose_name = '图文'
      verbose_name_plural = verbose_name



class MultilanguageInformation(BaseEntry):
    """
    图文多语言
    """
    information = models.ForeignKey(Information,on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"图文")
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name="多语言名称")
    language_code = models.CharField(max_length=50,null=False,default="chi",blank=True,verbose_name="语言编码")
    description = models.TextField(max_length=4096,null=True,verbose_name="描述")
    delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

    class Meta:
        verbose_name = "图文多语言"
        verbose_name_plural = verbose_name



class FileResource(BaseEntry):
    """
    文件资源
    """
    information = models.ForeignKey(Information,on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"图文")
    size = models.IntegerField(null=True,verbose_name="文件大小")
    resource_url = models.CharField(max_length=4096,null=False,default="", verbose_name="文件路径")
    original_name = models.TextField(max_length=100,null=False,default="",verbose_name="原文件名")
    name =  models.TextField(max_length=100,null=False,default="",verbose_name="文件名")
    delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

    class Meta:
        verbose_name = "文件资源"
        verbose_name_plural = verbose_name



class PosterResource(BaseEntry):
    """
    图片资源
    """
    information = models.ForeignKey(Information,on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"图文")
    size = models.IntegerField(null=True, verbose_name="文件大小")
    resource_url = models.CharField(max_length=4096 ,null=False,default="", verbose_name="文件路径")
    original_name = models.TextField(max_length=100,null=False,default="", verbose_name="原文件名")
    name = models.TextField(max_length=100,null=False,default="", verbose_name="文件名")
    horizontal_resoution = models.IntegerField(null=True, verbose_name="垂直分辨率")
    vertical_resoution = models.IntegerField(null=True, verbose_name="水平分辨率")
    delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

    class Meta:
        verbose_name = "图片资源"
        verbose_name_plural = verbose_name