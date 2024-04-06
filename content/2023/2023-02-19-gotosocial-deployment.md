Title: 部署 gotosocial
Date: 2023-02-19
Category: Tech
Tags: docker, gotosocial, mastodon, twitter, portainer

自马斯克收购 twitter 后幺蛾子不断，最近更是封杀了第三方客户端，这下我常用的 tweetbot 也不能用了。所以有些人已经开始转向其他平台了，其中以 mastodon 和 nostr 最为流行，我大概了解了一下两个平台，感觉 mastodon 的方式相对更为合理，所以也开始试用了一下。当然 nostr 的 damus 客户端我也下载试用了。

[mastodon](https://joinmastodon.org/) 只是基于 activitypub 协议的一种最为流行的实现。目前社区应该还挺活跃的，中文用户有很多。不过 mastodon 是使用 ruby 开发的，而且算是面向人数较多的一个大平台，我又想自己部署，所以又找了消耗资源相对较少的其他实现，这其中 [gotosocial](https://github.com/superseriousbusiness/gotosocial) 算是以此目的一种实现。我这里就只简单记录一下我自己是如何部署 gotosocial 的。

我之前已经有一套基于 [docker swarn 的环境](https://bobobo80.com/2021/ge-ren-fu-wu-qi-zi-dong-hua-bu-shu.html)，在此基础上新开一个 gotosocial 是非常简单快速的。官方文档给出了如何使用 docker 部署，我参考了 docker compose 的 yaml 文件创建了自己的 stacks 配置完成的部署。

- 先建好 volume，因为 gotosocial 使用 sqlite，还要存很多图片所以会占用比较大的空间，可以设置单独一个新的硬盘，如果你和我一样是使用低配 vps 的话，因为我的 vps 只有 10GB，加上系统和其他服务，剩余的空间不多了，所以我又单独加了一块硬盘空间给 gotosocial 使用。
- 新建 stacks，我是参考了官方的 yaml。network 是使用了已有的 nginx 网络，因为会由 nginx 转给相当于在 docker 内网的 gotosocial，所以 gotosocial 也不配置 https 证书，不设置 port。volume 使用上一步创建的 vol。剩下的就是 host 和 db type 和 db path 了，使用默认的就好。

```yaml
version: "3.3"

services:
  gotosocial:
    image: superseriousbusiness/gotosocial:latest
    networks:
      - nginx-net
    environment:
      GTS_HOST: mb.bobobo80.com
      GTS_DB_TYPE: sqlite
      GTS_DB_ADDRESS: /gotosocial/storage/sqlite.db
      GTS_LETSENCRYPT_ENABLED: "false"
      GTS_LETSENCRYPT_EMAIL_ADDRESS: ""
      ## For reverse proxy setups:
      # GTS_TRUSTED_PROXIES: "172.x.x.x"
    volumes:
      - gotosocial_data:/gotosocial/storage
    restart: "always"

volumes:
  gotosocial_data:
    external: true

networks:
  nginx-net:
    external: true
```

- stack 建好后，启动服务，gotosocial 就在 docker 内网里启动起来了。之后就是 nginx 的设置了，使用已有的 [nginx proxy manager](https://nginxproxymanager.com/)，把 mb.bobobo80.com 转发给 gotosocial 的 8080 端口（是 gotosocial 的默认端口），开启强制 https 并自动续期签名，就可以和外网连接起来了。
- gotosocial 的第一个用户是需要用命令行创建的，所以还要按照官网的命令创建第一个用户。

至此，整个 gotosocial 就算是搭建好了。因为 gotosocial 没有提供前端页面（实际是有几个页面的，但是不能发推），所以要使用其他客户登录，然后才能使用。我用网页版 pinafore 和 mastodon ios 客户端都可是正常使用。

最后，再说 2 个需要注意的地方。服务内存占用不大，我现在还没怎么使用内存占用应该再 20-50MB，不过硬盘占用会相对大一点，所以主要硬盘空间。第二点，目前 gotosocial 还没有开发迁移功能，现在还不能迁出，所以如果开始自己的服务时还是想好域名，因为一旦开始写内容了，发现域名不合适就改不了了。

欢迎关注我的 activitypub 账号@me@mb.bobobo80.com
