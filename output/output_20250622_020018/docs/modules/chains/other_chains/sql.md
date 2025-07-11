---
url: https://js.langchain.com.cn/docs/modules/chains/other_chains/sql
crawled_at: 2025-06-22T02:00:21.604126
---

SqlDatabaseChain
中文：
Sql数据库链
SqlDatabaseChain
可以让您在 SQL 数据库上回答问题。
此示例使用 Chinook 数据库，这是一个可用于 SQL Server、Oracle、MySQL 等的示例数据库。
设置
​
首先安装
typeorm
：
typeorm
包是必须安装的
npm
Yarn
pnpm
npm
install
typeorm
yarn
add
typeorm
pnpm
add
typeorm
然后安装所需的数据库依赖项。例如，对于 SQLite
npm
Yarn
pnpm
npm
install
sqlite3
yarn
add
sqlite3
pnpm
add
sqlite3
对于其他数据库，请参阅
https://typeorm.io/#installation
最后，按照
https://database.guide/2-sample-databases-sqlite/
上的说明，获取此示例所需的样品数据库。
import
{
DataSource
}
from
"typeorm"
;
import
{
OpenAI
}
from
"langchain/llms/openai"
;
import
{
SqlDatabase
}
from
"langchain/sql_db"
;
import
{
SqlDatabaseChain
}
from
"langchain/chains"
;
/**
* This example uses Chinook database, which is a sample database available for SQL Server, Oracle, MySQL, etc.
* To set it up follow the instructions on https://database.guide/2-sample-databases-sqlite/, placing the .db file
* in the examples folder.
*/
const
datasource
=
new
DataSource
(
{
type
:
"sqlite"
,
database
:
"Chinook.db"
,
}
)
;
const
db
=
await
SqlDatabase
.
fromDataSourceParams
(
{
appDataSource
:
datasource
,
}
)
;
const
chain
=
new
SqlDatabaseChain
(
{
llm
:
new
OpenAI
(
{
temperature
:
0
}
)
,
database
:
db
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
run
(
"How many tracks are there?"
)
;
console
.
log
(
res
)
;
// There are 3503 tracks.
您可以在创建
SqlDatabase
对象时包含或排除表格，以帮助链集中于您想要的表格。
它还可以减少链中使用的令牌数量。
const
db
=
await
SqlDatabase
.
fromDataSourceParams
(
{
appDataSource
:
datasource
,
includesTables
:
[
"Track"
]
,
}
)
;
如果需要，您可以在调用链时返回使用的 SQL 命令。
import
{
DataSource
}
from
"typeorm"
;
import
{
OpenAI
}
from
"langchain/llms/openai"
;
import
{
SqlDatabase
}
from
"langchain/sql_db"
;
import
{
SqlDatabaseChain
}
from
"langchain/chains"
;
/**
* This example uses Chinook database, which is a sample database available for SQL Server, Oracle, MySQL, etc.
* To set it up follow the instructions on https://database.guide/2-sample-databases-sqlite/, placing the .db file
* in the examples folder.
*/
const
datasource
=
new
DataSource
(
{
type
:
"sqlite"
,
database
:
"Chinook.db"
,
}
)
;
const
db
=
await
SqlDatabase
.
fromDataSourceParams
(
{
appDataSource
:
datasource
,
}
)
;
const
chain
=
new
SqlDatabaseChain
(
{
llm
:
new
OpenAI
(
{
temperature
:
0
}
)
,
database
:
db
,
sqlOutputKey
:
"sql"
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
"How many tracks are there?"
}
)
;
/* Expected result:
* {
*   result: ' There are 3503 tracks.',
*   sql: ' SELECT COUNT(*) FROM "Track";'
* }
*/
console
.
log
(
res
)
;