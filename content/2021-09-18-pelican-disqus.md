Title: Pelican集成disqus
Date: 2021-09-18
Category: Tech
Tags: pelican, disqus, github actions

虽然博客应该也不会有人留言，但是还是集成了一下disqus。这其中还挺坑的，一个找了很久。先说结论，应该是由于用了github actions自动发布，那个插件没有读取publishconf里的配置，导致siteurl是空，所以导致disqus的那个div没有显示。所以需要配置发布使用publishconf文件。

对于使用github actions自动push gh-pages分支，用到了这个nelsonjchen/gh-pages-pelican-action，这里面需要注意配置GITHUB_TOKEN，如果有自己域名，还要配置CNAME。

对于主题和插件，因为用到了git submodules，所以在github里也需要运行，通过git把依赖下下来，然后生成html
```bash
git submodule update --init --recursive
```

具体github actions文件可以参考[pelican github action](https://github.com/bobobo80/bobobo80-blog/blob/master/.github/workflows/main.yml)