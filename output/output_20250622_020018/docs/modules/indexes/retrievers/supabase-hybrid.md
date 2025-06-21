---
url: https://js.langchain.com.cn/docs/modules/indexes/retrievers/supabase-hybrid
crawled_at: 2025-06-22T02:00:23.310468
---

Supabase 混合搜索
Langchain 支持使用 Supabase Postgres 数据库进行混合搜索。该混合搜索结合了 Postgres 的
pgvector
扩展（相似度搜索)和全文搜索（关键词搜索)来检索文档。您可以通过 SupabaseVectorStore 的
addDocuments
函数添加文档。SupabaseHybridKeyWordSearch 接受嵌入， supabase 客户端， 相似性搜索的结果数量， 和关键词搜索的结果数量作为参数。
getRelevantDocuments
函数产生一个去重和按相关性分数排序的文档列表。
设置
​
安装库
​
npm
Yarn
pnpm
npm
install
-S @supabase/supabase-js
yarn
add
@supabase/supabase-js
pnpm
add
@supabase/supabase-js
在您的数据库中创建表和搜索函数
​
在您的数据库中运行以下内容:
-- Enable the pgvector extension to work with embedding vectors
create
extension vector
;
-- Create a table to store your documents
create
table
documents
(
id bigserial
primary
key
,
content
text
,
-- corresponds to Document.pageContent
metadata jsonb
,
-- corresponds to Document.metadata
embedding vector
(
1536
)
-- 1536 works for OpenAI embeddings, change if needed
)
;
-- Create a function to similarity search for documents
create
function
match_documents
(
query_embedding vector
(
1536
)
,
match_count
int
DEFAULT
null
,
filter jsonb
DEFAULT
'{}'
)
returns
table
(
id
bigint
,
content
text
,
metadata jsonb
,
similarity
float
)
language
plpgsql
as
$$
#variable_conflict use_column
begin
return
query
select
id
,
content
,
metadata
,
1
-
(
documents
.
embedding
<=>
query_embedding
)
as
similarity
from
documents
where
metadata @
>
filter
order
by
documents
.
embedding
<=>
query_embedding
limit
match_count
;
end
;
$$
;
-- Create a function to keyword search for documents
create
function
kw_match_documents
(
query_text
text
,
match_count
int
)
returns
table
(
id
bigint
,
content
text
,
metadata jsonb
,
similarity
real
)
as
$$
begin
return
query
execute
format
(
'select id, content, metadata, ts_rank(to_tsvector(content), plainto_tsquery($1)) as similarity
from documents
where to_tsvector(content) @@ plainto_tsquery($1)
order by similarity desc
limit $2'
)
using
query_text
,
match_count
;
end
;
$$
language
plpgsql
;
用法
​
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
import
{
createClient
}
from
"@supabase/supabase-js"
;
import
{
SupabaseHybridSearch
}
from
"langchain/retrievers/supabase"
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
client
=
createClient
(
process
.
env
.
SUPABASE_URL
||
""
,
process
.
env
.
SUPABASE_PRIVATE_KEY
||
""
)
;
const
embeddings
=
new
OpenAIEmbeddings
(
)
;
const
retriever
=
new
SupabaseHybridSearch
(
embeddings
,
{
client
,
//  Below are the defaults, expecting that you set up your supabase table and functions according to the guide above. Please change if necessary.
similarityK
:
2
,
keywordK
:
2
,
tableName
:
"documents"
,
similarityQueryName
:
"match_documents"
,
keywordQueryName
:
"kw_match_documents"
,
}
)
;
const
results
=
await
retriever
.
getRelevantDocuments
(
"hello bye"
)
;
console
.
log
(
results
)
;
}
;