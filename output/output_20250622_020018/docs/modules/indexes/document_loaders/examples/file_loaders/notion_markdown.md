---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/examples/file_loaders/notion_markdown
crawled_at: 2025-06-22T02:00:22.065792
---

Notion markdown export
本示例介绍如何从导出的 Notion 页面中加载数据。
首先，按照官方说明
这里
导出 Notion 页面为
Markdown & CSV
。确保选择
包括子页面
和
为子页面创建文件夹
。
然后，解压下载的文件并将未压缩的文件夹移动到存储库中。它应该包含你页面的 markdown 文件。
一旦文件夹在存储库中，只需运行下面的示例即可:
import
{
NotionLoader
}
from
"langchain/document_loaders/fs/notion"
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
/** Provide the directory path of your notion folder */
const
directoryPath
=
"Notion_DB"
;
const
loader
=
new
NotionLoader
(
directoryPath
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
console
.
log
(
{
docs
}
)
;
}
;