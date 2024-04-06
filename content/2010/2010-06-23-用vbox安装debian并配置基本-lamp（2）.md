title: 用vbox安装debian并配置基本应用（2）
date: 2010-06-23
categories: 计算机类
tags: linux,vbox

i80.be原创

首先修改语言环境，由于中文显不出来，所以索性就改成英文吧。

```
dpkg-reconfigure locales
```

由于vbox的NAT方式的网络连接不能让主机和虚拟机平级，所以要在vbox中再设置一个网卡，网络设置中再加如网络链接2，

[![](images/022734474.png)](http://www.shareapic.net/content.php?id=22734474) <!--more--> 如图，host-only adapt。

然后，应该要到dabian的网卡设置中设置一下，还好是DHCP，非常简单。

网卡设置：

```
vim /etc/network/interface
```

加入如下信息，就可以了，什么静态设置的，不懂，就不研究了：

auto eth1 iface eth1 inet dhcp

恩，ifconfig eth1 up应该就可以了，重启一下更保险。

好了，用ifconfig查看eth1的ip地址，应该是192.168.56.XX什么，在host里ping一下这个ip，一个1ms以内就应该是它了。

这时，host和虚拟机的连接就好了，用host的浏览器查看http://192.168.56.XX，恩，it works

恩，这就连上了。

有了这个基础，过几天可以再试试ssh连接，ftp连接什么的，应该都是可以的，越来越像远程操作了吧。等下篇继续。。。

i80.be原创
