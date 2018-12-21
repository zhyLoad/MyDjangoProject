from django.db import models



class Site(models.Model):
    url = models.CharField(max_length=100)


class User(models.Model):
    username = models.CharField(max_length=100)


class AccessKey(models.Model):
    key = models.CharField(max_length=100)


class Profile(models.Model):
    sites = models.ManyToManyField(Site)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    access_key = models.ForeignKey(AccessKey, on_delete=models.CASCADE,null=True, blank=True)


class Avatar(models.Model):
    image = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True,related_name='avatars')