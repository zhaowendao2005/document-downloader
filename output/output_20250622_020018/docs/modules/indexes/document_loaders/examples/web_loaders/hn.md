---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/examples/web_loaders/hn
crawled_at: 2025-06-22T02:00:22.574461
---

黑客新闻
本例介绍如何使用Cheerio从黑客新闻网站加载数据。每页将创建一个文档。
设置
​
npm
install
cheerio
用法
​
import
{
HNLoader
}
from
"langchain/document_loaders/web/hn"
;
const
loader
=
new
HNLoader
(
"https://news.ycombinator.com/item?id=34817881"
)
;
const
docs
=
await
loader
.
load
(
)
;