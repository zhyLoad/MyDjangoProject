
from django.db import models
from datetime import datetime



class Addresses(models.Model):
    """
    地址
    """
    ADDRESS_TYPE = (
        (1, "管理员地址"),
        (2, "用户住址"),
        (3, "用户收货地址"),
        (4, "门店地址"),
    )
    province = models.CharField(max_length=100, default="", verbose_name="省份")
    city = models.CharField(max_length=100, default="", verbose_name="城市")
    district = models.CharField(max_length=100, default="", verbose_name="区域")
    address_detail = models.CharField(max_length=100, default="", verbose_name="详细地址")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    address_type = models.IntegerField(choices=ADDRESS_TYPE,verbose_name="地址类型",help_text="1-管理员地址，2-用户住址，3-用户收货地址,4-门店地址")

    class Meta:
        verbose_name = "地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address_detail