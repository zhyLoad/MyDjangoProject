
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

user = get_user_model()



class BaseEntry(models.Model):
    """
    通用实体
    """
    create_time = models.DateTimeField(default=datetime.now,null=False, verbose_name="创建时间")
    creator = models.CharField(max_length=100, default=user,null=False, verbose_name="创建者")
    modify_time = models.DateTimeField(default=datetime.now,null=False, verbose_name="修改时间")
    modify = models.CharField(max_length=100, default=user,null=False, verbose_name="修改者")
    transaction_id = models.BigIntegerField(default= 1,verbose_name="事务ID")
    version = models.IntegerField(default= 1,verbose_name="版本号")

    class Meta:
     abstract = True
     ordering = ['create_time']



class Addresses(BaseEntry):
    """
    地址
    """
    ADDRESS_TYPE = (
        (1, "管理员地址"),
        (2, "用户住址"),
        (3, "用户收货地址"),
        (4, "门店地址"),
    )
    province = models.CharField(max_length=100, default="beijing",null=False, verbose_name="省份")
    city = models.CharField(max_length=100, default="beijing",null=False, verbose_name="城市")
    district = models.CharField(max_length=100, default="dongcheng",null=False, verbose_name="区域")
    address_detail = models.CharField(max_length=100, default="详细地址",null=False, verbose_name="详细地址")
    signer_mobile = models.CharField(max_length=11, default="", null=False,verbose_name="电话")
    address_type = models.IntegerField(choices=ADDRESS_TYPE,verbose_name="地址类型",null=False,help_text="1-管理员地址，2-用户住址，3-用户收货地址,4-门店地址")
    delete_flag = models.BooleanField(default=True, null=False, verbose_name="有效标识")

    class Meta:
        verbose_name = "地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address_detail


