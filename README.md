# MyDjangoProject

[![Build Status](https://travis-ci.org/mtianyan/hexoBlog-Github.svg?branch=master)](https://travis-ci.org/mtianyan/hexoBlog-Github)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

使用Python3.6与Django2.0.2(Django-rest-framework)以及前端vue开发的前后端分离的商城网站

项目支持支付宝支付(暂不支持微信支付),支持手机短信验证码注册， 支持第三方登录。集成了sentry错误监控系统。

>线上演示地址: http://vueshop.mtianyan.cn

## Quick Start

```
$ git clone https://github.com/zhyLoad/MyDjangoProject.git
$ cd MyDjangoProject
$ pip install -r requirements.txt
```

数据库文件(自行导入): vueshop.sql

use the address: http://127.0.0.1:8000/

## Contents：


对应教程已开通简书连载文集: https://www.jianshu.com/nb/22309475

**欢迎大家关注订阅，点赞！！！**

[原版视频课程地址:](https://coding.imooc.com/learn/list/131.html)

## About me

[简书](https://www.jianshu.com/u/db9a7a0daa1f) && [mtianyan's blog](http://blog.mtianyan.cn/)


欢迎关注简书，star项目！谢谢！






admin/admin123456





注意：Python3.6环境可能还需要安装如下安装包
social-auth-app-django
raven=6.7.0
djangorestframework=3.8.2
drf-extensions=0.3.1
django-redis=4.9.0
pycryptodome=3.6.1

django版本必须大于等于2.0


使用过程简述：
1.DownLoad代码，配置依赖包，需要的依赖包包括requirements.txt中和README.md中所有可能用到的包。
2.数据库创建好，并修改settings.py中的数据库配置项
3.终端进入虚拟环境，进行以下数据库更新和脚本执行命令：
   1） python manage.py makemigrations ----更新当前最新的表结构设计脚本
   2)  python manage.py migrate -----执行数据库建表操作
4.创建超级管理员，按照命令提示一步一步输入就可创建
    python manage.py createsuperuser
5.启动服务：
    python manage.py runserver
    启动后，浏览器键入:http://localhost:8000/xadmin，就可看到登录页面，键入superuser的用户名密码可登录
    键入http://localhost:8000，可以在浏览器看到所有Rest风格的API接口
6.其他数据脚本导入
   db_tools下有两个import_xxx.py文件，cd到该目录下（进入虚拟环境的前提下），执行python import_xxx.py，可将商品和目录相关的测试数据导入到数据库中。


遇到问题解决汇总：
1）Python3.6环境执行时总是报“AttributeError: 'NoneType' object has no attribute 'split'”
解决方案：https://stackoverflow.com/questions/21059640/wsgiref-error-attributeerror-nonetype-object-has-no-attribute-split
