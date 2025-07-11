---
url: https://js.langchain.com.cn/docs/modules/chains/index_related_chains/retrieval_qa
crawled_at: 2025-06-22T02:00:21.166096
---

检索问答
RetrievalQAChain
是将
Retriever
和 QA 链（上文中所述)组合起来的链。它用于从
Retriever
检索文档，然后使用
QA
链根据检索到的文档回答问题。
使用
​
在下面的示例中，我们使用
VectorStore
作为
Retriever
。默认情况下，将使用
StuffDocumentsChain
作为
QA
链。
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
HNSWLib
}
from
"langchain/vectorstores/hnswlib"
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
RecursiveCharacterTextSplitter
}
from
"langchain/text_splitter"
;
import
*
as
fs
from
"fs"
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
const
text
=
fs
.
readFileSync
(
"state_of_the_union.txt"
,
"utf8"
)
;
const
textSplitter
=
new
RecursiveCharacterTextSplitter
(
{
chunkSize
:
1000
}
)
;
const
docs
=
await
textSplitter
.
createDocuments
(
[
text
]
)
;
// Create a vector store from the documents.
const
vectorStore
=
await
HNSWLib
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
// Create a chain that uses the OpenAI LLM and HNSWLib vector store.
const
chain
=
RetrievalQAChain
.
fromLLM
(
model
,
vectorStore
.
asRetriever
(
)
)
;
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
使用自定义的
QA
链
​
在下面的示例中，我们使用
VectorStore
作为
Retriever
，并使用
RefineDocumentsChain
作为
QA
链。
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
,
loadQARefineChain
}
from
"langchain/chains"
;
import
{
HNSWLib
}
from
"langchain/vectorstores/hnswlib"
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
RecursiveCharacterTextSplitter
}
from
"langchain/text_splitter"
;
import
*
as
fs
from
"fs"
;
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
const
text
=
fs
.
readFileSync
(
"state_of_the_union.txt"
,
"utf8"
)
;
const
textSplitter
=
new
RecursiveCharacterTextSplitter
(
{
chunkSize
:
1000
}
)
;
const
docs
=
await
textSplitter
.
createDocuments
(
[
text
]
)
;
// Create a vector store from the documents.
const
vectorStore
=
await
HNSWLib
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
// Create a chain that uses a Refine chain and HNSWLib vector store.
const
chain
=
new
RetrievalQAChain
(
{
combineDocumentsChain
:
loadQARefineChain
(
model
)
,
retriever
:
vectorStore
.
asRetriever
(
)
,
}
)
;
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
output_text: '\n' +
'\n' +
"The president said that Justice Breyer has dedicated his life to serve his country, and thanked him for his service. He also said that Judge Ketanji Brown Jackson will continue Justice Breyer's legacy of excellence, emphasizing the importance of protecting the rights of citizens, especially women, LGBTQ+ Americans, and access to healthcare. He also expressed his commitment to supporting the younger transgender Americans in America and ensuring they are able to reach their full potential, offering a Unity Agenda for the Nation to beat the opioid epidemic and increase funding for prevention, treatment, harm reduction, and recovery."
}
}
*/