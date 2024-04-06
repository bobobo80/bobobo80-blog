title: 用vbox安装debian并配置基本应用（3）
date: 2010-06-25
categories: 计算机类
tags: linux,ssh,vbox,vsftpd

今天来配置ssh，和ftp。

因为[（2）](http://i80.be/105)中已经设置好了host与虚拟机的桥接，所以就可以通过ssh和ftp来管理虚拟机中的debian了。

这个两个东西都很好搞，强大的deb包管理，只需两条命令就可以了。<!--more-->

[ssh相关配置帮助](http://debian.linuxsir.org/doc/inthedebianway/openssh/openssh.debian.zh-3.html)

```
apt-get install openssh-server ssh
```

一些config复杂了，不那么在乎特别安全的话，默认就可以了吧。

在host里的终端

```
ssh root@192.168.56.XX
```

这里我出现了一个问题，在host里的终端ssh root@192.168.56.XX时，不能连接上

说什么RSA什么错误之类的吧，因为我前面和虚拟机里的以前的系统ssh过了，ip地址是一样的，所以RSA什么证书之类的就不一样了，所以要删除./.ssh/known\_hosts里的对应的那个密钥，麻烦的话把这个文件删了应该也成。

这样连接时就会出现yes/no选择，输入yes就会生成新密钥。就可以了

ftp用据说最简单的vsftpd

一条命令安装

```
apt-get install vsftpd
```

然后你就可以在host里用filezilla之类的匿名连接上了。

更复杂的设置要修改/etc/vsftpd.conf了

可以看看这个[用VSFTP搭建FTP服务器](http://hi.baidu.com/cassati/blog/item/3469bcfd12725c8eb901a0a7.html)，我就不那么了解了，不需要了解那么深。

再看看有什么其他的要配置，以后再说。

i80.be原创
