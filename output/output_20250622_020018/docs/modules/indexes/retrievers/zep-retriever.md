---
url: https://js.langchain.com.cn/docs/modules/indexes/retrievers/zep-retriever
crawled_at: 2025-06-22T02:00:23.426482
---

Zep Retriever
这个示例展示了如何在
RetrievalQAChain
中使用 Zep Retriever 从 Zep 内存存储中检索文档。(This example shows how to use the Zep Retriever in a
RetrievalQAChain
to retrieve documents from Zep memory store.)
设置(## Setup)
​
npm
Yarn
pnpm
npm
i @getzep/zep-js
yarn
add
@getzep/zep-js
pnpm
add
@getzep/zep-js
使用(## Usage)
​
import
{
ZepRetriever
}
from
"langchain/retrievers/zep"
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
url
=
process
.
env
.
ZEP_URL
||
"http://localhost:8000"
;
const
sessionId
=
"TestSession1232"
;
console
.
log
(
`
Session ID:
${
sessionId
}
, URL:
${
url
}
`
)
;
const
retriever
=
new
ZepRetriever
(
{
sessionId
,
url
}
)
;
const
query
=
"hello"
;
const
docs
=
await
retriever
.
getRelevantDocuments
(
query
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