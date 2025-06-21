---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/examples/file_loaders/docx
crawled_at: 2025-06-22T02:00:21.959510
---

Docx files
本示例介绍如何从docx文件中加载数据。
安装 Setup
npm
Yarn
pnpm
npm
install
mammoth
yarn
add
mammoth
pnpm
add
mammoth
用法 Usage
import
{
DocxLoader
}
from
"langchain/document_loaders/fs/docx"
;
const
loader
=
new
DocxLoader
(
"src/document_loaders/tests/example_data/attention.docx"
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