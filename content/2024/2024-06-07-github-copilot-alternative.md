Title: 使用continue替代github copilot
Date: 2024-06-07
Tag: github copilot, continue, vs code, llm, ai
Category: Tech

来了，又要发新一篇博客了。这次来讲一下最近使用[continue.dev](https://www.continue.dev)替代[github copilot](https://github.com/features/copilot)的使用感受。

# 背景
本来我是订阅的github copilot，每月10刀。虽然我的使用频率很低，不过我觉得还物有所值。不过因为其他一些原因，我还要使用另一个github账号，所以就导致另一个账号无法使用copilot，再买一份就有点贵了。于是我看了一下使用其他插件是不是也能达到相同的效果。

# 试用
我试了这么几款vs code插件和使用ai llm来进行代码补全和问答的插件。
* [continue.dev](https://www.continue.dev)
* [TabbyML](https://tabby.tabbyml.com)
* [twinny](https://github.com/rjmacarthy/twinny)
* [privy](https://github.com/srikanth235/privy)

这几个应该是开源的支持自定义api的代码补全和问答的插件。这里面privy是主打本地模型，不联网。而Tabby是团队自部署模型服务，还带一个后台管理系统。twinny看文档，其目的也是主要用于连接自建ollama模型，provider里都没有openai，不过支持litellm，可以间接转发。

所以基本只剩下一家continue了。continue可以说是一个高度自定义的插件了，即可接入外部云服务的ai接口，也支持ollama或类似本地或内部网络的llm api。不过目前代码补全部分还是beta阶段。

另外还有一些插件，比如b站上说的比较多的codegpt，也是支持本地和线上服务。但是是闭源的，就没有试用。

# 本地ollama
因为我的电脑配置很差，所以我使用公司的电脑也测试了一下本地[ollama](https://ollama.com)的效果，但是公司的MBP2019配置也好不到哪去，所以效果也不是很好。使用6.7b的[deepseek coder instruct](https://ollama.com/library/deepseek-coder:6.7b)回答代码问题，要4-5分钟。更崩溃的是使用1b的[starcoder](https://ollama.com/library/starcoder)做代码补全，初始速度是10-20s。然后代码敲起来之后多并发会慢到4，5分钟才出结果，根本无法使用。

# continue使用情况
基本上所有插件都是分两个接口，一个是问答的，一个补全代码的，continue也一样。这是因为[常规的llm没有对代码补全这种形式做微调，可能效果并不好](https://docs.continue.dev/walkthroughs/tab-autocomplete#i-want-better-completions-should-i-use-gpt-4)，所以会单独设置一个给代码补全的专门的模型。
问答型可以有多种模式，比如chatgpt式的问，或者嵌套一个模版，来重构代码，写测试，修改等。而代码补全就和最早的copilot一样，在敲代码停顿时会显示灰色的ai生成代码，如果确认接受这些自动补全，那么按tab填写了这些代码了。目前continue还是偏重问答式，如果是类似cursor那种框选然后让ai不断生成修改的方式编程的话，continue支持的不错，比如选中你需要修改的那一段代码，然后出发edit问答，向ai说出你的要求，在收到ai的回答后，continue会diff显示ai结果和当前的区别，像处理merge conflicts一样，你可以一段一段的选择accept current还是incoming。极端的情况就是你可以不断地问和下指令，不断修改和填充，就像人写代码一样，只不过换成了ai。另外，continue也支持提供一些上下文来作为问答的上下文（有点绕），比如提供某个代码文件，整个工程（在copilot里是workspace），文档等，这样不光你的问题是prompt，插件也会讲与问题相关的代码，文档一起提供给模型参考。这里面为了提供更贴切的上下文，continue会对项目代码做索引，就是先embedding本地代码，然后提交时，会搜索相关度高的部分作为上下文。所以这里会有后台任务一直在索引代码变更，我在公司电脑试用时发现会导致卡顿，可能是公司项目太大了，同时总是切换分支（切换分支会导致开新的索引），配置差应该也是一个原因。个人的小项目没有感觉到卡顿。
代码补全我觉得一方面和copilot差不多，都是在使用第三方库时，补全的内容可能离预期差很多，感觉上下文的处理不是很好。另外请求量挺大的，不是很清楚触发机制。按插件的统计，token的使用，自动补全占大头。

# 模型
模型也是分成问答和代码补全两部分。
## 代码补全模型
代码补全相对特殊，常规模型可能没有良好的适配训练，工作的并不是很好。大家比较常用的是[starcoder](https://ollama.com/library/starcoder2)，[deepseek-coder-base](https://ollama.com/library/deepseek-coder)，[codellama](https://ollama.com/library/codellama)，以及新发布的[codestral](https://mistral.ai/news/codestral/)，另外好像[codeqwen-base](https://ollama.com/library/codeqwen)也是适用的。这些应该都是开源模型，可以本地运行，也可以使用在线服务商的，不过很多服务商是没有这些模型的serverless服务的，得找找，自己部署就不合算了。根据continue的推荐，我用过[fireworks.ai](https://fireworks.ai)的starcoder 7b，速度很快，很流畅，价格是0.2刀输入输出每百万token，是很便宜了，即使补全消耗的比较大，消耗的也是比较慢的。deepseek官方注册给的credit太少，只试了两句问答就没了，另外官方只有chat和coder两种模型，你也不知道他是base模型还是instruct模型。然后还有赛博菩萨[cloudflare worker ai的deepseek-coder-base 6.7b](https://developers.cloudflare.com/workers-ai/models/deepseek-coder-6.7b-base-awq/)，因为有每日免费额度，当前这个模型还在beta，免费！不过我在使用中会总出现多返回了<end of sentence>还没有查是什么原因。另外还有，codestral是mistral新出的特别给代码微调的模型大小是22b，我没有注册mistral，还没有试用，价格是1刀输入3刀输出每百万token，是fireworks starcoder的5倍多了。我没有配置高的电脑，从其他人的反馈看，本地运行小尺寸的模型应该问题也不大，本地运行3b或1b的starcoder或deepseek应该都不错。后面随着npu推广，本地运行这些小模型都会非常流畅了。
## 问答模型
问答模型就可以使用各种常规模型了，选择非常多。比如御三家openai或gemini，或claud的模型，从评测上看gpt-4依然是最好的？不过好像对于复杂问题，claud opus的风评最好。低价的选择有[together.ai](https://www.together.ai)的deepseek-coder-33b和phind-34b，之前的codestral也可以。免费的选择有[groq](https://groq.com)，有限量的llama3-70b，是比较适合代码问答的，而且巨快。然后cloudflare只有[6.7b的deepseek-coder-instruct](https://developers.cloudflare.com/workers-ai/models/deepseek-coder-6.7b-instruct-awq/)，模型大小小了点，准确性差一点。

## embeddings模型
其实还有第三种模型（貌似现在有第四种rerank）embeddings模型。就是使用什么模型来计算代码的向量，这决定了是否能够提供更相似的上下文给问答或补全模型。现在continue有三种选项，transformers.js是本地计算；nomic-embed-text是通过ollama；voyage-code-2是云端付费商业模型。我只使用了本地transformers模型，就先不做评价了。

# 未来
这两天高通，amd，intel都上市或发布了高TOPS npu的cpu产品，未来本地算力会越来越高。像代码补全和embeddings这类模型本地运行应该会非常普遍了。我也该考虑更新一下我的电脑了。