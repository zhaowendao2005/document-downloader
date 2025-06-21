---
url: https://js.langchain.com.cn/docs/ecosystem/databerry
crawled_at: 2025-06-22T02:00:19.507719
---

数据莓
本页面介绍如何在LangChain中使用
Databerry
。
什么是数据莓？
​
数据莓是一个
开源
的文档检索平台，帮助连接您的个人数据和大型语言模型。
快速开始
​
从LangChain中检索存储在数据莓中的文档非常容易！
import
{
DataberryRetriever
}
from
"langchain/retrievers/databerry"
;
const
retriever
=
new
DataberryRetriever
(
{
datastoreUrl
:
"https://api.databerry.ai/query/clg1xg2h80000l708dymr0fxc"
,
apiKey
:
"DATABERRY_API_KEY"
,
// optional: needed for private datastores
topK
:
8
,
// optional: default value is 3
}
)
;
// Create a chain that uses the OpenAI LLM and Databerry retriever.
const
chain
=
RetrievalQAChain
.
fromLLM
(
model
,
retriever
)
;
// Call the chain with a query.
const
res
=
await
chain
.
call
(
{
query
:
"What's Databerry?"
,
}
)
;
console
.
log
(
{
res
}
)
;
/*
{
res: {
text: 'Databerry provides a user-friendly solution to quickly setup a semantic search system over your personal data without any technical knowledge.'
}
}
*/