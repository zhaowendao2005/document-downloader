---
url: https://js.langchain.com.cn/docs/modules/indexes/vector_stores/integrations/weaviate
crawled_at: 2025-06-22T02:00:24.668231
---

Weaviate
Weaviate是一个开源的向量数据库，可以存储对象和向量，使向量搜索与结构化过滤相结合。LangChain通过
weaviate-ts-client
软件包连接到Weaviate，这是官方的Typescript客户端。
LangChain直接将向量插入Weaviate并查询给定向量的最近邻，因此您可以使用所有LangChain Embeddings与Weaviate的集成。
设置
​
npm
Yarn
pnpm
npm
install
weaviate-ts-client graphql
yarn
add
weaviate-ts-client graphql
pnpm
add
weaviate-ts-client graphql
您需要在本地或服务器上运行Weaviate，请参阅
Weaviate文档
获取更多信息。
用法：插入文档
​
/* eslint-disable @typescript-eslint/no-explicit-any */
import
weaviate
from
"weaviate-ts-client"
;
import
{
WeaviateStore
}
from
"langchain/vectorstores/weaviate"
;
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
export
async
function
run
(
)
{
// Something wrong with the weaviate-ts-client types, so we need to disable
const
client
=
(
weaviate
as
any
)
.
client
(
{
scheme
:
process
.
env
.
WEAVIATE_SCHEME
||
"https"
,
host
:
process
.
env
.
WEAVIATE_HOST
||
"localhost"
,
apiKey
:
new
(
weaviate
as
any
)
.
ApiKey
(
process
.
env
.
WEAVIATE_API_KEY
||
"default"
)
,
}
)
;
// Create a store and fill it with some texts + metadata
await
WeaviateStore
.
fromTexts
(
[
"hello world"
,
"hi there"
,
"how are you"
,
"bye now"
]
,
[
{
foo
:
"bar"
}
,
{
foo
:
"baz"
}
,
{
foo
:
"qux"
}
,
{
foo
:
"bar"
}
]
,
new
OpenAIEmbeddings
(
)
,
{
client
,
indexName
:
"Test"
,
textKey
:
"text"
,
metadataKeys
:
[
"foo"
]
,
}
)
;
}
用法：查询文档
​
/* eslint-disable @typescript-eslint/no-explicit-any */
import
weaviate
from
"weaviate-ts-client"
;
import
{
WeaviateStore
}
from
"langchain/vectorstores/weaviate"
;
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
export
async
function
run
(
)
{
// Something wrong with the weaviate-ts-client types, so we need to disable
const
client
=
(
weaviate
as
any
)
.
client
(
{
scheme
:
process
.
env
.
WEAVIATE_SCHEME
||
"https"
,
host
:
process
.
env
.
WEAVIATE_HOST
||
"localhost"
,
apiKey
:
new
(
weaviate
as
any
)
.
ApiKey
(
process
.
env
.
WEAVIATE_API_KEY
||
"default"
)
,
}
)
;
// Create a store for an existing index
const
store
=
await
WeaviateStore
.
fromExistingIndex
(
new
OpenAIEmbeddings
(
)
,
{
client
,
indexName
:
"Test"
,
metadataKeys
:
[
"foo"
]
,
}
)
;
// Search the index without any filters
const
results
=
await
store
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
results
)
;
/*
[ Document { pageContent: 'hello world', metadata: { foo: 'bar' } } ]
*/
// Search the index with a filter, in this case, only return results where
// the "foo" metadata key is equal to "baz", see the Weaviate docs for more
// https://weaviate.io/developers/weaviate/api/graphql/filters
const
results2
=
await
store
.
similaritySearch
(
"hello world"
,
1
,
{
where
:
{
operator
:
"Equal"
,
path
:
[
"foo"
]
,
valueText
:
"baz"
,
}
,
}
)
;
console
.
log
(
results2
)
;
/*
[ Document { pageContent: 'hi there', metadata: { foo: 'baz' } } ]
*/
}