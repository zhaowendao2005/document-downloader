---
url: https://js.langchain.com.cn/docs/modules/indexes/vector_stores/integrations/prisma
crawled_at: 2025-06-22T02:00:24.486026
---

prisma
sidebar_label: 仅适用于 node
​
Prisma
Langchain 支持使用
Prisma
与 PostgreSQL 和
pgvector
Postgres 扩展来增强 PostgreSQL 数据库中的现有模型的向量搜索。
设置
​
使用 Supabase 设置数据库实例
​
请参阅
Prisma 和 Supabase 集成指南
来设置 Supabase 和 Prisma 的新数据库实例。
安装 Prisma
​
npm
Yarn
pnpm
npm
install
prisma
yarn
add
prisma
pnpm
add
prisma
使用
docker-compose
设置
pgvector
自托管实例
​
pgvector
提供了一个预构建的 Docker 映像，可用于快速设置自托管的 Postgres 实例。
services
:
db
:
image
:
ankane/pgvector
ports
:
-
5432
:
5432
volumes
:
-
db
:
/var/lib/postgresql/data
environment
:
-
POSTGRES_PASSWORD=
-
POSTGRES_USER=
-
POSTGRES_DB=
volumes
:
db
:
创建新模型
​
Create a new schema
​
假设您还没有创建一个模型，使用类型为
Unsupported("vector")
的
vector
字段创建一个新模型:
model Document {
id      String                 @id @default(cuid())
content String
vector  Unsupported("vector")?
}
然后，使用
--create-only
创建新的迁移，以避免直接运行迁移。
Afterwards, create a new migration with
--create-only
to avoid running the migration directly.
npm
Yarn
pnpm
```bash npm2yarn
npx prisma migrate dev --create-only
```bash
npm
undefined
# couldn't auto-convert command2yarn
npx prisma migrate dev --create-only
```bash
npm
undefined
# couldn't auto-convert command2yarn
npx prisma migrate dev --create-only
添加以下行到新创建的迁移，以启用
pgvector
扩展，如果它尚未被启用:
Add the following line to the newly created migration to enable
pgvector
extension if it hasn't been enabled yet:
CREATE
EXTENSION
IF
NOT
EXISTS
vector
;
然后运行迁移:
Run the migration afterwards:
npm
Yarn
pnpm
```bash npm2yarn
npx prisma migrate dev
```bash
npm
undefined
# couldn't auto-convert command2yarn
npx prisma migrate dev
```bash
npm
undefined
# couldn't auto-convert command2yarn
npx prisma migrate dev
使用
​
:::警告
表名和列名（例如
tableName
、
vectorColumnName
、
columns
和
filter
中的字段)直接传递到 SQL 查询中，没有参数化。这些字段必须在使用前进行净化以避免 SQL 注入。
These fields must be sanitized beforehand to avoid SQL injection.
:::
import
{
PrismaVectorStore
}
from
"langchain/vectorstores/prisma"
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
PrismaClient
,
Prisma
,
Document
}
from
"@prisma/client"
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
db
=
new
PrismaClient
(
)
;
// Use the `withModel` method to get proper type hints for `metadata` field:
const
vectorStore
=
PrismaVectorStore
.
withModel
<
Document
>
(
db
)
.
create
(
new
OpenAIEmbeddings
(
)
,
{
prisma
:
Prisma
,
tableName
:
"Document"
,
vectorColumnName
:
"vector"
,
columns
:
{
id
:
PrismaVectorStore
.
IdColumn
,
content
:
PrismaVectorStore
.
ContentColumn
,
}
,
}
)
;
const
texts
=
[
"Hello world"
,
"Bye bye"
,
"What's this?"
]
;
await
vectorStore
.
addModels
(
await
db
.
$transaction
(
texts
.
map
(
(
content
)
=>
db
.
document
.
create
(
{
data
:
{
content
}
}
)
)
)
)
;
const
resultOne
=
await
vectorStore
.
similaritySearch
(
"Hello world"
,
1
)
;
console
.
log
(
resultOne
)
;
// create an instance with default filter
const
vectorStore2
=
PrismaVectorStore
.
withModel
<
Document
>
(
db
)
.
create
(
new
OpenAIEmbeddings
(
)
,
{
prisma
:
Prisma
,
tableName
:
"Document"
,
vectorColumnName
:
"vector"
,
columns
:
{
id
:
PrismaVectorStore
.
IdColumn
,
content
:
PrismaVectorStore
.
ContentColumn
,
}
,
filter
:
{
content
:
{
equals
:
"default"
,
}
,
}
,
}
)
;
await
vectorStore2
.
addModels
(
await
db
.
$transaction
(
texts
.
map
(
(
content
)
=>
db
.
document
.
create
(
{
data
:
{
content
}
}
)
)
)
)
;
// Use the default filter a.k.a {"content": "default"}
const
resultTwo
=
await
vectorStore
.
similaritySearch
(
"Hello world"
,
1
)
;
console
.
log
(
resultTwo
)
;
// Override the local filter
const
resultThree
=
await
vectorStore
.
similaritySearchWithScore
(
"Hello world"
,
1
,
{
content
:
{
equals
:
"different_content"
}
}
)
;
console
.
log
(
resultThree
)
;
}
;
上述示例使用以下模式:：
// This is your Prisma schema file,
// learn more about it in the docs: https://pris.ly/d/prisma-schema
generator client {
provider = "prisma-client-js"
}
datasource db {
provider = "postgresql"
url      = env("DATABASE_URL")
}
model Document {
id        String                 @id @default(cuid())
content   String
namespace String?                @default("default")
vector    Unsupported("vector")?
}
如果不需要，你可以删除
namespace
。