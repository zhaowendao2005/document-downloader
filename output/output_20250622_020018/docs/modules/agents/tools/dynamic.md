---
url: https://js.langchain.com.cn/docs/modules/agents/tools/dynamic
crawled_at: 2025-06-22T02:00:20.836226
---

DynamicTool
自定义工具
创建运行自定义代码的工具的一种选项是使用
DynamicTool
。
DynamicTool
类需要输入一个名称， 一个描述， 和一个函数。
重要的是， 名称和描述将被语言模型用来确定何时调用此函数以及使用哪些参数来调用它，
因此，请确保将它们设置为一些语言模型可以理解的值！
提供的函数是代理程序实际调用的函数。当发生错误时， 应该，在可能的情况下，返回表示错误的字符串，而不是抛出错误。
这允许错误被传递到 LLM 并且 LLM 可以决定如何处理它。如果抛出错误，那么代理程序的执行将停止。
请参阅下面的示例以定义和使用
DynamicTool
。
import
{
OpenAI
}
from
"langchain/llms/openai"
;
import
{
initializeAgentExecutorWithOptions
}
from
"langchain/agents"
;
import
{
DynamicTool
}
from
"langchain/tools"
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
DynamicTool
(
{
name
:
"FOO"
,
description
:
"call this to get the value of foo. input should be an empty string."
,
func
:
(
)
=>
"baz"
,
}
)
,
new
DynamicTool
(
{
name
:
"BAR"
,
description
:
"call this to get the value of bar. input should be an empty string."
,
func
:
(
)
=>
"baz1"
,
}
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
}
)
;
console
.
log
(
"Loaded agent."
)
;
const
input
=
`
What is the value of foo?
`
;
console
.
log
(
`
Executing with input "
${
input
}
"...
`
)
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
console
.
log
(
`
Got output
${
result
.
output
}
`
)
;
}
;