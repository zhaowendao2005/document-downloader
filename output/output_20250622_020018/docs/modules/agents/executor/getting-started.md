---
url: https://js.langchain.com.cn/docs/modules/agents/executor/getting-started
crawled_at: 2025-06-22T02:00:20.381334
---

代理执行器(Agent Executors)
代理使用LLM来确定采取哪些操作以及采取的顺序。操作可以是使用工具并观察其输出，或返回给用户。
正确使用代理可以非常强大。在本教程中,我们将向您展示如何通过最简单的,最高级别的API轻松使用代理。
为了加载代理,您应该了解以下概念:
工具:(Tool)  执行特定职责的函数。这可以是像:谷歌搜索(Google Search)，数据库查找(Database lookup)，代码REPL，其他链。工具的接口目前是预期具有字符串输入，和字符串输出的函数。
LLM: 代理支持的语言模型。
代理: 代理以使用。这应该是一个字符串，引用支持的代理类。因为这个笔记本集中在最简单的,最高级别的API上，所以仅涵盖使用标准支持的代理。
对于这个例子,您需要在
.env
文件中设置SerpAPI环境变量。
SERPAPI_API_KEY
=
"..."
现在，我们可以开始了！(Now we can get started!)
import
{
initializeAgentExecutorWithOptions
}
from
"langchain/agents"
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
SerpAPI
}
from
"langchain/tools"
;
import
{
Calculator
}
from
"langchain/tools/calculator"
;
const
model
=
new
OpenAI
(
{
temperature
:
0
}
)
;
const
tools
=
[
new
SerpAPI
(
process
.
env
.
SERPAPI_API_KEY
,
{
location
:
"Austin,Texas,United States"
,
hl
:
"en"
,
gl
:
"us"
,
}
)
,
new
Calculator
(
)
,
]
;
const
executor
=
await
initializeAgentExecutorWithOptions
(
tools
,
model
,
{
agentType
:
"zero-shot-react-description"
,
verbose
:
true
,
}
)
;
const
input
=
`
Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?
`
;
const
result
=
await
executor
.
call
(
{
input
}
)
;
langchain-examples:start: Executing with input
"Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?"
..
.
langchain-examples:start: Got output Harry Styles is Olivia Wilde's boyfriend and his current age raised to the
0.23
power is
2.169459462491557
.