from django.db import models


class Tenant(models.Model):
     """
       租户信息
     """

     TENANT_STATUS = (
         (1, "可用"),
         (2, "冻结"),
     )

     name =  models.CharField(max_length=100, null=False, blank=True, verbose_name="租户名称")
     phone = models.CharField(max_length=20, null=False, blank=True, verbose_name="租户电话")
     email = models.CharField(max_length=500, null=False, blank=True, verbose_name="租户邮箱")
     status = models.IntegerField(choices=TENANT_STATUS,null=False, blank=True, verbose_name="租户状态")

     class Meta:
         verbose_name = '租户'
         verbose_name_plural = verbose_name

     def __str__(self):
         return self.name

class Manager(models.Model):
     """
       管理员信息
     """
     name =  models.CharField(max_length=100, null=False, blank=True, verbose_name="管理员名称")
     phone = models.CharField(max_length=20, null=False, blank=True, verbose_name="电话")
     email = models.CharField(max_length=500, null=False, blank=True, verbose_name="邮箱")
     tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name=u"租户")

     class Meta:
         verbose_name = '管理员'
         verbose_name_plural = verbose_name

class Organization(models.Model):
    """
    组织机构
    """
    name = models.CharField(max_length=100, null=False, blank=True, verbose_name="机构名称")
    parent_id = models.BigIntegerField(null=False,default=-1,verbose_name="父机构ID")
    phone = models.CharField(max_length=20, null=False, blank=True, verbose_name="电话")
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name=u"租户")

    class Meta:
        verbose_name = '组织机构'
        verbose_name_plural = verbose_name