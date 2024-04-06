title: 用vbox安装debian并配置基本应用（1）
date: 2010-06-23
categories: 计算机类
tags: lamp,linux,vbox

i80.be原创

今日闲来无事，开始折腾。

想来自己用linux已经有点年头了，但水平还是很菜，一直都是只玩桌面，不玩命令。

自己搞博客刚开始，发现对linux的底层的东西了解甚少，计划未来也可能自己玩vps，所以先训练一下吧。

vbox虚拟机在ubuntu下很好安装，加源，apt即可，不多说了。<!--more-->

我下载了debian最小的网络安装iso，40+M，然后设置好NAT网络链接模式，这里下载﻿http://[www.debian.org/distrib/netinst](http://www.debian.org/distrib/netinst)

iso加入到vbox中启动，弱弱的选择了图形化安装，一路和ubuntu安装差不多，有趣的是校园对于中国那个源相应速度特别的快，所以我也没有改源。安装哪些包只选择了标准系统，没有选数据库什么的。 装好了root登录，不用update了，因为是网络安装。都是源里最新的。改装LAMP了。我是参考U坛里这篇[http://forum.ubuntu.org.cn/viewtopic.php?f=43&t=219318](http://forum.ubuntu.org.cn/viewtopic.php?f=43&t=219318)

不过我没有在命令行中找到lamp-server这个组合包，貌似得用新立德才行，所以要分别安装。按那个贴的顺序来：

```
apt-get install ssh
```

```
apt-get install mysql-server
```

```
apt-get install apache2
```

```
apt-get install php5 libapache2-mod-php5
```

然后重启apache服务

```
/etc/init.d/apache2 restart
```

安装phpmyadmin

```
apt-get install phpmyadmin
```

如何测试apache?由于没有X，所以这里用w3m

```
w3m localhost
```

OK，显示it works

（按上文）测试mysql

```
netstat -tap | grep mysql
```

应该显示tcp 0 0 localhost.localdomain:mysql \*:\* LISTEN -

测试PHP debian的根目录位于/var/www中 在里面添加一个测试文件test.php文件，内容 <?php phpinfo(); ?> 浏览器重输入http://localhost/test.php ，看到php信息网页，则说明PHP安装成功

里面的编辑部分都用vim了，虽然我也不会用vi，基本的打字还是能用的。

先写到这，等会写下，如何在主机host的浏览器上查看/var/www/的内容。

i80.be原创
