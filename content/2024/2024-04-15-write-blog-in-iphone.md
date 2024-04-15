Title: 在iPhone上写博客
Date: 2024-04-15
Tag: pelican, iSH, markdown
Category: Tech

是因为使用了新的工作流来写博客，以及因为在上班路上带入耳式耳机导致发炎，所以停止了在路上听播客的活动。

所以目前在上班路上就是刷刷手机，如果有想写点什么，就用手机来码字了。[上一篇博客](https://bobobo80.com/2024/quan-yun-duan-kai-fa-huan-jing.html)就是在手机上写的。虽然手机上直接使用github codespace也能直接打开，但实际操作体验并不好，一个是屏幕小，界面操作不方便，打字时直接一半屏幕被占用，也看不清。然后没有比如鼠标右键，拖拽等操作。所以我开始找在ios上编写markdown的工具。

# markdown on iphone
我在app store里搜索markdown，会有一堆软件，不过很多要收费或内购。我没有一一尝试，在一堆app中我看到了[mweb](https://apps.apple.com/sg/app/mweb-markdown-%25E5%2586%2599%25E4%25BD%259C-%25E7%25AC%2594%25E8%25AE%25B0%25E5%2592%258C%25E5%258F%2591%25E5%25B8%2583/id1183407767?l=zh-Hans-CN)，之前听[播客](https://talk.swift.gg/1)，[draveness](https://draveness.me)有讲到使用mweb写博客，我点进去查看，发现作者还有一款轻量级的markdown软件，[one markdown](https://apps.apple.com/sg/app/one-markdown/id1507139439?l=zh-Hans-CN)，买断或订阅比mweb便宜很多。我是很轻量使用的，所以就直接选择了这个试试。因为没用过其他app，所以没有对比。我还没有付费，主要的功能是在输入框上面加了一行常用的工具按钮栏，可以快速插入需要的格式。然后有预览功能，同时可以接入iphone的文件系统，直接在onedrive或其他网盘目录编写。这很重要，因为这使得它能集成进git工具，在git目录里编辑md文件。

# Git on iphone
在iphone上写博客除了编辑，还需要发布。好在我之前解决了[自动生成和发布](https://bobobo80.com/2021/pelicanji-cheng-disqus.html)，所以现在要做的就是把编辑好的md文件push到master分支，github action会自动完成新内容发布。而在iphone使用git，比较常用的工具应该是[working copy](https://apps.apple.com/sg/app/working-copy-git-client/id896694807?l=zh-Hans-CN)，是图形化的工具，看起来甚至自带文本编辑，不知道有没有markdown的特殊优化。而这个app是买断收费，我还在观察我是否需要，只为了手机写博客这个场景不太值得。然后我找到了免费的方法，就是使用终端工具，我有安装[iSH](https://apps.apple.com/sg/app/ish-shell/id1436902243?l=zh-Hans-CN)，里面可以命令行运行各种命令，是个alpine linux沙盒，再安装git就可以使用了。连接github需要ish中生成ssh key，然后在github设置public key，就可以了。

所以，完整的流程就是one markdown中在iSH的博客项目pelican content中创建一个新md文件，编辑好之后。再到ish中git add/commit/push。就是可以完成新文章的发布了！