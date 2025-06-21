---
url: https://js.langchain.com.cn/docs/modules/indexes/vector_stores/integrations/chroma
crawled_at: 2025-06-22T02:00:23.874988
---

chroma
换行符
Chroma（嵌入式的开源Apache 2.0数据库)
Chroma是一个开源的Apache 2.0嵌入式数据库。
设置
​
在计算机上使用Docker运行Chroma
文档
安装Chroma JS SDK。
npm
Yarn
pnpm
npm
install
-S chromadb
yarn
add
chromadb
pnpm
add
chromadb
使用，索引和查询文档
​
import
{
Chroma
}
from
"langchain/vectorstores/chroma"
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
// Create vector store and index the docs
const
vectorStore
=
await
Chroma
.
fromDocuments
(
docs
,
new
OpenAIEmbeddings
(
)
,
{
collectionName
:
"a-test-collection"
,
}
)
;
// Search for the most similar document
const
response
=
await
vectorStore
.
similaritySearch
(
"hello"
,
1
)
;
console
.
log
(
response
)
;
/*
[
Document {
pageContent: 'Foo\nBar\nBaz\n\n',
metadata: { source: 'src/document_loaders/example_data/example.txt' }
}
]
*/
使用，索引和查询文本
​
import
{
Chroma
}
from
"langchain/vectorstores/chroma"
;
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
// text sample from Godel, Escher, Bach
const
vectorStore
=
await
Chroma
.
fromTexts
(
[
`
Tortoise: Labyrinth? Labyrinth? Could it Are we in the notorious Little
Harmonic Labyrinth of the dreaded Majotaur?
`
,
"Achilles: Yiikes! What is that?"
,
`
Tortoise: They say-although I person never believed it myself-that an I
Majotaur has created a tiny labyrinth sits in a pit in the middle of
it, waiting innocent victims to get lost in its fears complexity.
Then, when they wander and dazed into the center, he laughs and
laughs at them-so hard, that he laughs them to death!
`
,
"Achilles: Oh, no!"
,
"Tortoise: But it's only a myth. Courage, Achilles."
,
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
collectionName
:
"godel-escher-bach"
,
}
)
;
const
response
=
await
vectorStore
.
similaritySearch
(
"scared"
,
2
)
;
console
.
log
(
response
)
;
/*
[
Document { pageContent: 'Achilles: Oh, no!', metadata: {} },
Document {
pageContent: 'Achilles: Yiikes! What is that?',
metadata: { id: 1 }
}
]
*/
// You can also filter by metadata
const
filteredResponse
=
await
vectorStore
.
similaritySearch
(
"scared"
,
2
,
{
id
:
1
,
}
)
;
console
.
log
(
filteredResponse
)
;
/*
[
Document {
pageContent: 'Achilles: Yiikes! What is that?',
metadata: { id: 1 }
}
]
*/
使用，从现有集合查询文档
​
import
{
Chroma
}
from
"langchain/vectorstores/chroma"
;
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
const
vectorStore
=
await
Chroma
.
fromExistingCollection
(
new
OpenAIEmbeddings
(
)
,
{
collectionName
:
"godel-escher-bach"
}
)
;
const
response
=
await
vectorStore
.
similaritySearch
(
"scared"
,
2
)
;
console
.
log
(
response
)
;
/*
[
Document { pageContent: 'Achilles: Oh, no!', metadata: {} },
Document {
pageContent: 'Achilles: Yiikes! What is that?',
metadata: { id: 1 }
}
]
*/