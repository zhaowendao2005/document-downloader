---
url: https://js.langchain.com.cn/docs/modules/indexes/retrievers/remote-retriever
crawled_at: 2025-06-22T02:00:23.181788
---

远程检索器
本示例展示如何在
RetrievalQAChain
中使用远程检索器从远程服务器检索文档。
使用
​
import
{
OpenAI
}
from
"langchain/llms/openai"
;
import
{
RetrievalQAChain
}
from
"langchain/chains"
;
import
{
RemoteLangChainRetriever
}
from
"langchain/retrievers/remote"
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
// Initialize the LLM to use to answer the question.
const
model
=
new
OpenAI
(
{
}
)
;
// Initialize the remote retriever.
const
retriever
=
new
RemoteLangChainRetriever
(
{
url
:
"http://0.0.0.0:8080/retrieve"
,
// Replace with your own URL.
auth
:
{
bearer
:
"foo"
}
,
// Replace with your own auth.
inputKey
:
"message"
,
responseKey
:
"response"
,
}
)
;
// Create a chain that uses the OpenAI LLM and remote retriever.
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
"What did the president say about Justice Breyer?"
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
text: 'The president said that Justice Breyer was an Army veteran, Constitutional scholar,
and retiring Justice of the United States Supreme Court and thanked him for his service.'
}
}
*/
}
;