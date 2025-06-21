---
url: https://js.langchain.com.cn/docs/modules/agents/
crawled_at: 2025-06-22T02:00:19.608488
---

代理人
info
概念指南
一些应用程序需要的不仅是预先确定的调用LLMs/其他工具的链，但可能是依赖于用户输入的未知链。在这些类型的链中，存在一个“代理人”，其可以访问一组工具。根据用户输入，代理人可以决定是否以及如何调用这些工具。
目前有两种主要类型的代理人:
动作代理人
: 这些代理人决定要采取的行动并一步一步地采取这些行动
计划执行代理人
: 这些代理人首先决定要执行的一系列行动计划，然后逐一执行这些行动。
你应该何时使用它们？
动作代理人更为常规，适合处理小任务。
对于更复杂或长期运行的任务，计划执行代理人的初始规划步骤有助于保持长期目标和关注点，但通常需要更多的调用和更高的延迟。
这两种代理人也不是互斥的 - 实际上，通常最好由动作代理人负责执行计划和执行代理人。
动作代理人
​
一个动作代理人的高级伪代码如下:
接收一些用户输入
代理人
决定使用哪个
工具
（如果有的话），以及该工具的输入应该是什么。
使用
工具输入
调用那个
工具
，并记录
观察结果
（这只是调用该
工具输入
的输出)。
将
工具
的历史记录、
工具输入
和
观察结果
传回到
代理程序
，然后它决定下一步该怎么做。
重复上述步骤，直到
代理程序
决定不再需要使用
工具
，然后直接回应用户。
interface
AgentStep
{
action
:
AgentAction
;
observation
:
string
;
}
interface
AgentAction
{
tool
:
string
;
// Tool.name
toolInput
:
string
;
// Tool.call argument
}
interface
AgentFinish
{
returnValues
:
object
;
}
class
Agent
{
plan
(
steps
:
AgentStep
[
]
,
inputs
:
object
)
:
Promise
<
AgentAction
|
AgentFinish
>
;
}
计划和执行代理
​
计划和执行代理的高级伪代码大致如下:
接收到一些用户输入
计划者列出要采取的步骤
执行者逐个执行步骤，直到输出最终结果
当前实现的方式是使用LLMChain作为计划者，使用Action Agent作为执行者。
深入了解
​
🗃️
代理
3 items
🗃️
Agent Executors
1 items
🗃️
工具
7 items
🗃️
工具包
4 items
📄️
其他功能
我们为Agents提供了许多其他功能。您还应查看LLM-specific features和Chat Model-specific features。