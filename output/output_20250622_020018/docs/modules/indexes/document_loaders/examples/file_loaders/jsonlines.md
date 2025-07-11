---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/examples/file_loaders/jsonlines
crawled_at: 2025-06-22T02:00:22.024838
---

JSONLines 文件
这个例子演示了如何从 JSONLines 或 JSONL 文件加载数据。第二个参数是一个 JSONPointer，用于从文件中的每个 JSON 对象中提取属性。每个 JSON 对象都将创建一个文档。
示例 JSONLines 文件:
{
"html"
:
"This is a sentence."
}
{
"html"
:
"This is another sentence."
}
示例代码:
import
{
JSONLinesLoader
}
from
"langchain/document_loaders/fs/json"
;
const
loader
=
new
JSONLinesLoader
(
"src/document_loaders/example_data/example.jsonl"
,
"/html"
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
/*
[
Document {
"metadata": {
"blobType": "application/jsonl+json",
"line": 1,
"source": "blob",
},
"pageContent": "This is a sentence.",
},
Document {
"metadata": {
"blobType": "application/jsonl+json",
"line": 2,
"source": "blob",
},
"pageContent": "This is another sentence.",
},
]
*/