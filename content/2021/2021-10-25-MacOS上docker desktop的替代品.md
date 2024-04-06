Title: MacOS 上 docker desktop 的替代品
Date: 2021-10-25
Category: Tech
Tags: docker, portainer, lima, podman, macos

最近，也不算太近，docker desktop 宣布要改变授权，对于商业用途且具有一定的规模的话，明年就要开始收费了。很多公司都是使用 mac 作为开发电脑的，虽然对于大公司的话应该也会管这个 docker 费用的，但是我还是在 mac 上试用了其他的两个替代方案，折腾了一下。

## lima

在 docker 要收费的消息出来不久，就有一篇[ntt 写的文章介绍 lima](https://medium.com/nttlabs/containerd-and-lima-39e0b64d2a59)。另外还有中文的翻译稿。搜索引擎搜索的排名也很高。我也就尝试安装了 lima。安装非常简单，brew 一条命令就安装上了，

```bash
brew install lima
```

安装好之后要用 lima 创建一个虚拟机，可以先使用 default 配置，命令如下

```bash
limactl start
```

这个时间会稍微有点长，然后虚拟机就创建好了。然后就可以使用了，基本就是使用 lima nerdctl 来代替 docker，使用 docker 的各种 run，pull，images 什么的，比如

```bash
lima nerdctl ps --all
```

这里 lima 其实是创建了一个 linux 虚拟机，在 Mac 的任务管理器里，能看到一个 qemu 的检查，那个就是虚拟机了。

### 坑

这里注意一个问题是，那个 ntt 的文章里后面还写了 GUI，rancher desktop。但是实际上，这个 rancher 和 brew 安装的 lima 是分离的，不在一起。在安装和启动 rancher desktop 后，rancher 会在再创建一个虚拟机，给你安装 nerdctl 和 k3s 的环境，实际上 rancher desktop 是用 lima 再建一个虚拟机，并提供另一套 nerdctl 和 k3s 环境。rancher desktop 启动后，在命令行输入的 nerdctl 是 rancher 的 nerdctl，而用 lima nerdctl 是自己安装 lima 的 nerdctl。而且 rancher desktop 提供的功能和 docker desktop 也不太一样。只提供了 k8s 的版本，images，和系统资源占用的配置。docker 里的 container dashboard 是没有的。

## podman

lima 的方案相当于是 lima 虚拟机+containerd 的方案。还有另一个方案现在在 Mac 上也可以运行了，那就是 podman。可以参考(podman 的文档进行安装和设置)[https://podman.io/getting-started/installation]。

```bash
brew install podman
```

安装好后，用 podman machine 命令创建和启动虚拟机就可以了

```bash
podman machine init
podman machine start
```

之后，就是使用 podman 命令代替 docker 了。

```bash
podman ps --all
```

有个(podman 的 GUI 工具)[https://github.com/heyvito/podman-macos]，可以显示当前的 containers，但是我试用了下，会导致 cpu 使用率高，不知道是什么原因。不过之前提到的 portainer 是支持 podman 的，可以用 portainer 来管理 posman。这里注意 docker run 里需要加上 privileged 参数，同时 docker.sock 对应的 volume 也变成了 podman.sock。这样就能用本地的 9000 端口（或者换成自己需要的端口）来管理 docker 了。

```bash
podman run -d -p 9000:9000 --privileged --name=portainer --restart=always -v /run/user/1000/podman/podman.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```

两个工具都是先起一个 linux 虚拟机，lima 是 ubuntu，podman 是 fedora（podman 背后是 redhat 出的）。然后各自在其虚拟机开始 containerd 和 podman 环境来替代 docker。

## 后续

由于公司的项目中有用到用旧版本来编译 protobuf 文件，所以使用 docker 来创建就版本 protoc 环境就比较方便了，因为还有新项目用新版本 protoc，使用 docker 的不同镜像可以分离不同的环境。这时 podman 这个工具就不行了，因为 podman 在 mac 下还不支持挂载 mac 下的目录，就是说 podman 的容器读取不到 mac 的文件，所以，无法像 docker 一样，用容器的运行环境，读取宿主机的 protobuf 文件，然后生成对应的比如 pb.go 文件到宿主机上。而 lima 是可以的，不过在生成 pb.go 文件到宿主机这一步，需要开启一个写宿主机文件的权限。 ~/.lima/default/lima.yaml 例如如果是默认设置是这个文件，然后修改 mount 下的 write 为 true 就可以了。
