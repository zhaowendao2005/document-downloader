---
url: https://js.langchain.com.cn/docs/modules/indexes/retrievers/vectorstore
crawled_at: 2025-06-22T02:00:23.254650
---

向量库
一旦您创建了一个
向量库
， ,使用它作为检索器就非常简单:
vectorStore
=
...
retriever
=
vectorStore
.
asRetriever
(
)