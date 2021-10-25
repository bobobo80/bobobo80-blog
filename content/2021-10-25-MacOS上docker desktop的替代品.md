Title: MacOS上docker desktop的替代品
Date: 2021-10-25
Category: Tech
Tags: docker, portainer, lima, podman, macos

最近，也不算太近，docker desktop宣布要改变授权，对于商业用途且具有一定的规模的话，明年就要开始收费了。很多公司都是使用mac作为开发电脑的，虽然对于大公司的话应该也会管这个docker费用的，但是我还是在mac上试用了其他的两个替代方案，折腾了一下。

## lima
在docker要收费的消息出来不久，就有一篇[ntt写的文章介绍lima](https://medium.com/nttlabs/containerd-and-lima-39e0b64d2a59)。另外还有中文的翻译稿。搜索引擎搜索的排名也很高。我也就尝试安装了lima。安装非常简单，brew一条命令就安装上了，
```bash
brew install lima
```
安装好之后要用lima创建一个虚拟机，可以先使用default配置，命令如下
```bash
limactl start
```
这个时间会稍微有点长，然后虚拟机就创建好了。然后就可以使用了，基本就是使用lima nerdctl来代替docker，使用docker的各种run，pull，images什么的，比如
```bash
lima nerdctl ps --all
```
这里lima其实是创建了一个linux虚拟机，在Mac的任务管理器里，能看到一个qemu的检查，那个就是虚拟机了。

### 坑
这里注意一个问题是，那个ntt的文章里后面还写了GUI，rancher desktop。但是实际上，这个rancher和brew安装的lima是分离的，不在一起。在安装和启动rancher desktop后，rancher会在再创建一个虚拟机，给你安装nerdctl和k3s的环境，实际上rancher desktop是用lima再建一个虚拟机，并提供另一套nerdctl和k3s环境。rancher desktop启动后，在命令行输入的nerdctl是rancher的nerdctl，而用lima nerdctl是自己安装lima的nerdctl。而且rancher desktop提供的功能和docker desktop也不太一样。只提供了k8s的版本，images，和系统资源占用的配置。docker里的container dashboard是没有的。

## podman
lima的方案相当于是lima虚拟机+containerd的方案。还有另一个方案现在在Mac上也可以运行了，那就是podman。可以参考(podman的文档进行安装和设置)[https://podman.io/getting-started/installation]。
```bash
brew install podman
```
安装好后，用podman machine命令创建和启动虚拟机就可以了
```bash
podman machine init
podman machine start
```
之后，就是使用podman命令代替docker了。
```bash
podman ps --all
```
有个(podman的GUI工具)[https://github.com/heyvito/podman-macos]，可以显示当前的containers，但是我试用了下，会导致cpu使用率高，不知道是什么原因。不过之前提到的portainer是支持podman的，可以用portainer来管理posman。这里注意docker run里需要加上privileged参数，同时docker.sock对应的volume也变成了podman.sock。这样就能用本地的9000端口（或者换成自己需要的端口）来管理docker了。
```bash
podman run -d -p 9000:9000 --privileged --name=portainer --restart=always -v /run/user/1000/podman/podman.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```
两个工具都是先起一个linux虚拟机，lima是ubuntu，podman是fedora（podman背后是redhat出的）。然后各自在其虚拟机开始containerd和podman环境来替代docker。