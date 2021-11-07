Title: Linux 配置 kinto 快捷键
Date: 2021-11-07
Category: Tech
Tags: linux, kinto, shortcut, manjaro, xkeysnail

时隔多年，我又转回使用 linux 作为个人桌面系统了。主要是目前在使用 win10 时，wsl 性能不是很好，本身笔记本配置比较差，是 amd 的 2500 和 8G 内存，导致在使用 vs coderemote 到 wsl2 开发时，format 都总是卡住。同时又想折腾一下 linux 桌面了（对了，主要是想折腾了），所以我又把 linux 装回来了。在刚买这个笔记本时，其实已经安装过 linux，只不过由于驱动原因，放弃了。我的本是联想 lenovo 720s AMD 版，cpu 是 2500 内存 8G 焊死。在刚买来是安装 linux 一个是网卡驱动需要单独下载驱动包，这个问题还好。另一个问题是总是卡死，只能强行关机重启。可能是哪个地方的驱动不太行。当时试了 ubuntu 和 manjaro，都是一样。

这期间我已经换了网卡，因为那个原装 rtl8821ce 本身就不太行，在 windows 下也总是掉线。所以换了个 intel 的网卡。所以这次安装 linux 非常顺利，开箱即用。这次我选了 manjaro kde 版本。

其他折腾 linux 桌面也没什么可说的。这里主要记录一些我修改了一点点 kinto.sh 配置。

[Kinto.sh](https://kinto.sh/)是一个修改键盘映射的工具，可以把 windows 和 linux 的键盘布局改成类似 Mac 的键盘布局，同时还真对一些常用软件的快捷键做了特殊的设置。

由于工作用的是 Mac，所以快捷键已经比较习惯 mac 的方式。尤其是那个 cmd+cv 系列。回到 win 或 linux 改用 ctrl 会很不习惯。而如果你直接报 ctrl 和 alt 调换的话，又有很多快捷键会变化，比如 alt+tab。所以还是用工具比较方便。

Kinto 还可以调整 windows 的快捷键，但是我还没有试过，所以先只说 linux。我这个本的键盘最下面从左到右 4 个键依次是 Ctrl-Fn-Win-Alt。Fn 是不能改的。从 mac 迁移过来的习惯当然是，把 alt 改成 ctrl，这样复制粘贴就是 alt+cv 了。同时想浏览器什么的，就是 alt+w 关闭，+r 刷新什么的。Kinto.sh 中这种方式是叫 windows&apple。会将 alt 变成 ctrl，win 变成 alt，ctrl 变成 win。但是在使用终端软件时，会将 alt 变成 ctrl+shift，win 还是 alt，ctrl 还是 ctrl，这样在终端下的复制粘贴就还是使用 alt+cv。kinto 的配置会用针对各种软件的一些单独配置。

## 我的一些特殊需求

对于 ctrl 和 alt 的改动，kinto 已经满足了我的需求。不过我还习惯把 capslock 本身功能屏蔽掉，并且让 capslock 按下时，可以使用 hjkl 来当成上下左右键。我查了一下 kinto 依赖的 xkeysnail，应该是并不支持这种设定，因为[capslock 不是 modifier](https://github.com/mooz/xkeysnail/pull/33)。不过我通过把 capslock 先改成其他键，间接地实现了这种我的需求。

kinto.sh 提供了 kinto.py，也就是 kinto config。我可以修改里面的配置来达到自己的目的。
先修改 define_multipurpose_modmap，把 capslock 换成右 ctrl

```python
define_multipurpose_modmap(
    {Key.CAPSLOCK: [Key.RIGHT_CTRL, Key.RIGHT_CTRL] # custom
    # {Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]   # Enter2Cmd
    # {Key.CAPSLOCK: [Key.ESC, Key.RIGHT_CTRL]  # Caps2Esc
    # {Key.LEFT_META: [Key.ESC, Key.RIGHT_CTRL] # Caps2Esc - Chromebook
    # {                                         # Placeholder
})
```

然后修改 General GUI 的配置，加上 ctrl+hjkl 的快捷键变成上下左右。

```python
# None referenced here originally
# - but remote clients and VM software ought to be set here
# These are the typical remaps for ALL GUI based apps
define_keymap(lambda wm_class: wm_class.casefold() not in remotes,{
    # K("RC-Space"): K("Alt-F1"),                   # Default SL - Launch
    ...
    K("C-j"): K("Down"),
    K("C-h"): K("Left"),
    K("C-k"): K("Up"),
    K("C-l"): K("Right"),
}, "General GUI")
```

General GUI 的第一行配置也可以注释掉。这个应该是会影响到输入法切换。

好了。这样就结束了。虽然这样会占用 ctrl+hjkl 的快捷键，可能会一些软件的快捷键，但是，这样已经是我试验过的比较好的解决方案了。因为把 capslock 换成 win 或 alt 都有有其他一些影响。而 kinto 依赖的 xkeysnail 又不支持将 capslock 单独变成 modifier，或是把 capslock 换成多个 modifier 组合。所以只能是换成 ctrl 对整体使用影响较小。同时需要注意的是，由于修改了 define_multipurpose_modmap，所以如果使用 kinto 自带的 tweak 设置，会导致配置文件错误，需要手工修复。所以在配置文件修改好后，就不要动 tweak 了。
