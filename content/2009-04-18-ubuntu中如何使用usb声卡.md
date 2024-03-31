title: ubuntu中如何使用usb声卡
date: 2009-04-18
categories: 计算机类

台式机板载声卡杂音很大，于是斥巨资20元搞了个usb外置声卡。在ubuntu下虽然插上能自动识别，测试音效有声。但是音乐播放器还是没声音。搜索发现，原来是没有设置成默认声卡。  
  
http://forum.ubuntu.org.cn/viewtopic.php?f=42&t=142956  
现摘录设置方法如下：  
如何在ubuntu中设置默认声卡：  
\* 首先 sudo asoundconf list  
会列出声卡的名字，如  
Headset （我的罗技USB声卡被识别成了耳机）   //我的是Adapter  
V8237  
\* 然后，如果想把Headset设成默认声卡：  
sudo asoundconf set-default-card Headset   //sudo asoundconf set-default-card Adapter  
  
注1：如果无效的话，去掉sudo再试一次  
注2：原文说需要重启，但我没有重启也成功了  
  
以后相关ubuntu设置文章将发布于simple ubuntu博客，这里只提供链接。
