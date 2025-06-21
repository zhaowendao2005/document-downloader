---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/examples/file_loaders/text
crawled_at: 2025-06-22T02:00:22.152375
---

文本文件
本例将介绍如何从文本文件中加载数据。
import
{
TextLoader
}
from
"langchain/document_loaders/fs/text"
;
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