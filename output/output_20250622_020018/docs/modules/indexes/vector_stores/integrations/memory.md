---
url: https://js.langchain.com.cn/docs/modules/indexes/vector_stores/integrations/memory
crawled_at: 2025-06-22T02:00:23.957393
---

MemoryVectorStore
MemoryVectorStore是一个内存中的暂存向量存储器，用于在内存中存储嵌入，并做精确的线性搜索以找到最相似的嵌入。默认的相似度度量是余弦相似度，但可以更改为
ml-distance
支持的任何相似度度量方式。
用法
​
从文本创建新索引
​
import
{
MemoryVectorStore
}
from
"langchain/vectorstores/memory"
;
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
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
vectorStore
=
await
MemoryVectorStore
.
fromTexts
(
[
"Hello world"
,
"Bye bye"
,
"hello nice world"
]
,
[
{
id
:
2
}
,
{
id
:
1
}
,
{
id
:
3
}
]
,
new
OpenAIEmbeddings
(
)
)
;
const
resultOne
=
await
vectorStore
.
similaritySearch
(
"hello world"
,
1
)
;
console
.
log
(
resultOne
)
;
}
;
从加载程序创建新索引
​
import
{
MemoryVectorStore
}
from
"langchain/vectorstores/memory"
;
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
import
{
TextLoader
}
from
"langchain/document_loaders/fs/text"
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
// Create docs with a loader
const
loader
=
new
TextLoader
(
"src/document_loaders/example_data/example.txt"
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
// Load the docs into the vector store
const
vectorStore
=
await
MemoryVectorStore
.
fromDocuments
(
docs
,
new
OpenAIEmbeddings
(
)
)
;
// Search for the most similar document
const
resultOne
=
await
vectorStore
.
similaritySearch
(
"hello world"
,
1
)
;
console
.
log
(
resultOne
)
;
}
;
使用自定义相似度度量
​
import
{
MemoryVectorStore
}
from
"langchain/vectorstores/memory"
;
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
import
{
similarity
}
from
"ml-distance"
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
vectorStore
=
await
MemoryVectorStore
.
fromTexts
(
[
"Hello world"
,
"Bye bye"
,
"hello nice world"
]
,
[
{
id
:
2
}
,
{
id
:
1
}
,
{
id
:
3
}
]
,
new
OpenAIEmbeddings
(
)
,
{
similarity
:
similarity
.
pearson
}
)
;
const
resultOne
=
await
vectorStore
.
similaritySearch
(
"hello world"
,
1
)
;
console
.
log
(
resultOne
)
;
}
;