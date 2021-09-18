Title: 使用Django+Vue组合开发Restful风格的家用收纳系统
Date: 2017-06-26
Category: Tech
Tags: django, python

为了进一步学习web开发相关内容，自己想了个需求，就开始干了。
[github项目链接](https://github.com/bobobo80/RightThingsInRightPlaces)
构架采用流行的RESTful api风格后端加响应式前端组合，虽然都还不熟悉，但是硬着头皮开始。
经过一番调研，Django Rest framework（drf）算是比较广泛的restful库了，看了看文档，比较清晰，在序列化方面有一些便捷的方法。
后端验证方面，使用了drf文档里推荐的oauth toolkit库来组合。
前端方面，许久之前只是了解一些基本的前端东西，html/css/js不是很熟，但有基本概念。
既然要搞高端的响应式，那么对比一下流行的react/vue/augular发现前端一套套框架啊工具啊又是很深的坑，选了看起来可以用最简单方式的单vue的方式来开发。
对于初学者，感觉还是不要在基础薄弱的情况下就直接开始，文档中很多东西都不知道。

目前算是完成了第一个阶段，基础的文件夹和物品结构和查增改删，tag标签设置，用户登录等，
后面还有搜索功能需要探索一下。然后在全面学习一下前端之后，再来完善一轮前端后端。

我把现在的版本部署到了[pythonanywhere](http://bobobo80.pythonanywhere.com)
