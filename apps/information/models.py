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
  tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE,default='', verbose_name=u"租户")
  audit_reason = models.CharField(max_length=2048, null=True, blank=True, verbose_name="审核原因")
  delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

  class Meta:
      verbose_name = '图文'
      verbose_name_plural = verbose_name



class MultilanguageInformation(BaseEntry):
    """
    图文多语言
    """
    information = models.ForeignKey(Information,on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"图文",related_name="multi_language_informations")
    name = models.CharField(max_length=100,null=True,blank=True,verbose_name="多语言名称")
    language_code = models.CharField(max_length=50,null=False,default="chi",blank=True,verbose_name="语言编码")
    description = models.TextField(max_length=4096,null=True,verbose_name="描述")
    delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

    class Meta:
        verbose_name = "图文多语言"
        verbose_name_plural = verbose_name

#文件资源类型：1-文件；2-图片；3-文本
FILE_TYPE_CHOICES = ((1, 'file'), (2, 'poster'), (3, 'txt'))

class FileResource(BaseEntry):
    """
    文件资源
    """
    information = models.ForeignKey(Information,on_delete=models.CASCADE,null=True, blank=True,verbose_name=u"图文",related_name="file_resources")
    type = models.SmallIntegerField(choices=FILE_TYPE_CHOICES,
                                       default=2,
                                       help_text="file type")
    file = models.FileField(upload_to='.', blank=True)
    delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

    class Meta:
        verbose_name = "文件资源"
        verbose_name_plural = verbose_name



