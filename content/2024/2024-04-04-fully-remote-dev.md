title: 全云端开发环境
date: 2024-04-04
category: Tech
tags: github, codespace

我目前在用的笔记本电脑还是19年买的amd ryzen 2500加8G板载内存，cpu还够用，但如果日常学习和开发的话经常会内存不够（是的cook，8g内存真的不够），因为windows一般要开个wsl，会挺占内存的。换成linux的话，有两个硬件相关的问题，一个是时不时突然卡住死机，一个是盒盖休眠或关机后开盖无法唤醒。然后也试了[chrome os flex](https://chromeos.google/products/chromeos-flex/)，一个给非chromebook的chrome os系统。但是续航又有问题，满电状态只有2小时的续航时间。因为现在也没有多少时间用电脑，所以还不想换新的（主要是没钱）。

以前在字节以及shopee初期，是有个人的远程开发机的，所以我也试着使用云端的方案来做个人开发。

调查发现比较出名的是[gitpod](https://www.gitpod.io)和[github codespace](https://github.com/features/codespaces)，还有可以自己部署的[coder](https://coder.com)。这些都算是基于vs code改动的项目。另外google cloud和aws还有他们的云端开发环境，不过我没有尝试。coder要自己部署，在vps上其实不太合适，如果是连接到自己的台式机或者物理服务器上可能还比较适用。剩下两个云端的，因为codespace是github自家的，另外免费时间比较长，所以就选择了github codespace。

体验上来说还不错，延迟什么的不明显。就是快捷键有些好像和local版的不一样或者是浏览器的快捷键冲突。打开速度也比较满意，因为实际上是他们后台需要把你的这个虚拟机开机的，有个启动过程，可能有5-10s？有时候会遇到golang的语言服务故障，高亮显示或者函数跳转无效，需要重开一下网页。调试方面也比较方便，会分配一个域名，然后端口可以设置公开或需要auth验证。插件也都可以使用vs code的插件。终端我是使用了vscode里面的终端，可以安装fish，我平时是用fish shell。

免费时长是60小时每月，最低配置2核8g，配置加倍时间减半。对于我完全够用，因为现在根本没什么时间。

其他工具，postman也是用web版，而且因为不用call本地接口，所以也不用装浏览器插件了。然后装个终端工具[hyper](https://hyper.is)连接vps调试。就这些了。没有本地vscode，没有本地go python环境，没有wsl。浏览器+终端就是所有了。哦，chrome可以给codespace和postman的pwa模式开单独的图标，方便在任务栏切换。

在播客teahour目前的[最后一期](https://teahour.fm/95)里是嘉宾介绍如何使用chromebook做开发，其实原理就是使用远程工作站+vim开发。不过我仍然需要图形化的节目，随着vscode的发展，web版也是非常可用的了。目前常规的除了客户端开发可能还是本地更合适，web前后端远程的形式已经相当可用了。如果你感兴趣，也来试一试吧。

