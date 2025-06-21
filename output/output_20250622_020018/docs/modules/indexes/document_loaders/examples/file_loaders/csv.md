---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/examples/file_loaders/csv
crawled_at: 2025-06-22T02:00:21.776904
---

CSV文件
本示例介绍如何从CSV文件加载数据。
第二个参数是要从CSV文件中提取的“列”名称。每行CSV文件将创建一个文档。
当未指定“列”时，每一行都将转换为一个键/值对，并将每个键/值对输出到文档的“pageContent”中的新行中。
当指定了“列”时，将为每一行创建一个文档，并将指定列的值用作文档的“pageContent”。
备注：该处的“pageContent”指文档的页面内容)
设置
​
npm
Yarn
pnpm
npm
install
d3-dsv@2
yarn
add
d3-dsv@2
pnpm
add
d3-dsv@2
用法-提取所有列
​
示例CSV文件:
id,text
1,This is a sentence.
2,This is another sentence.
示例代码:
import
{
CSVLoader
}
from
"langchain/document_loaders/fs/csv"
;
const
loader
=
new
CSVLoader
(
"src/document_loaders/example_data/example.csv"
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
"line": 1,
"source": "src/document_loaders/example_data/example.csv",
},
"pageContent": "id: 1
text: This is a sentence.",
},
Document {
"metadata": {
"line": 2,
"source": "src/document_loaders/example_data/example.csv",
},
"pageContent": "id: 2
text: This is another sentence.",
},
]
*/
用法-提取单个列
​
示例CSV文件:
id,text
1,This is a sentence.
2,This is another sentence.
示例代码:
import
{
CSVLoader
}
from
"langchain/document_loaders/fs/csv"
;
const
loader
=
new
CSVLoader
(
"src/document_loaders/example_data/example.csv"
,
"text"
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
"line": 1,
"source": "src/document_loaders/example_data/example.csv",
},
"pageContent": "This is a sentence.",
},
Document {
"metadata": {
"line": 2,
"source": "src/document_loaders/example_data/example.csv",
},
"pageContent": "This is another sentence.",
},
]
*/