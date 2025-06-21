---
url: https://js.langchain.com.cn/docs/modules/indexes/retrievers/databerry-retriever
crawled_at: 2025-06-22T02:00:23.036930
---

Databerry Retriever
本示例展示如何在
RetrievalQAChain
中使用Databerry Retriever从Databerry.ai数据存储库检索文档。
Usage使用方法
​
import
{
DataberryRetriever
}
from
"langchain/retrievers/databerry"
;
export
const
run
=
async
(
)
=>
{
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
const
docs
=
await
retriever
.
getRelevantDocuments
(
"hello"
)
;
console
.
log
(
docs
)
;
}
;