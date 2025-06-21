---
url: https://js.langchain.com.cn/docs/modules/agents/executor/
crawled_at: 2025-06-22T02:00:20.356066
---

Agent Executors
info
概念指南
为了让智能代理更加强大，我们需要使其迭代，即调用模型多次，直到达到最终答案。这就是 AgentExecutor 的工作。
class
AgentExecutor
{
// a simplified implementation
run
(
inputs
:
object
)
{
const
steps
=
[
]
;
while
(
true
)
{
const
step
=
await
this
.
agent
.
plan
(
steps
,
inputs
)
;
if
(
step
instanceof
AgentFinish
)
{
return
step
.
returnValues
;
}
steps
.
push
(
step
)
;
}
}
}
📄️
开始(Getting Started)
代理使用LLM来确定采取哪些操作以及采取的顺序。操作可以是使用工具并观察其输出，或返回给用户。