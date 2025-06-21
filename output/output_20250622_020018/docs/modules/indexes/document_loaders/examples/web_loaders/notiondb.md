---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/examples/web_loaders/notiondb
crawled_at: 2025-06-22T02:00:22.593648
---

Notion数据库
本示例演示了如何从Notion数据库加载数据。
你需要你的Notion集成令牌和要访问的资源的“databaseId”。
不要忘记将你的集成添加到数据库中！
import
{
NotionDBLoader
}
from
"langchain/document_loaders/web/notiondb"
;
const
loader
=
new
NotionDBLoader
(
{
pageSizeLimit
:
10
,
databaseId
:
"databaseId"
,
notionIntegrationToken
:
"<your token here>"
,
// Or set as process.env.NOTION_INTEGRATION_TOKEN
}
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