---
url: https://js.langchain.com.cn/docs/modules/agents/agents/action/conversational_agent
crawled_at: 2025-06-22T02:00:19.992369
---

会话代理
本示例介绍如何为聊天模型创建会话代理。它将利用聊天特定的提示。
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
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
export
const
run
=
async
(
)
=>
{
process
.
env
.
LANGCHAIN_HANDLER
=
"langchain"
;
const
model
=
new
ChatOpenAI
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
// Passing "chat-conversational-react-description" as the agent type
// automatically creates and uses BufferMemory with the executor.
// If you would like to override this, you can pass in a custom
// memory option, but the memoryKey set on it must be "chat_history".
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
"chat-conversational-react-description"
,
verbose
:
true
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
input0
=
"hi, i am bob"
;
const
result0
=
await
executor
.
call
(
{
input
:
input0
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
result0
.
output
}
`
)
;
const
input1
=
"whats my name?"
;
const
result1
=
await
executor
.
call
(
{
input
:
input1
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
result1
.
output
}
`
)
;
const
input2
=
"whats the weather in pomfret?"
;
const
result2
=
await
executor
.
call
(
{
input
:
input2
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
result2
.
output
}
`
)
;
}
;
Loaded agent.
Entering new agent_executor chain...
{
"action": "Final Answer",
"action_input": "Hello Bob! How can I assist you today?"
}
Finished chain.
Got output Hello Bob! How can I assist you today?
Entering new agent_executor chain...
{
"action": "Final Answer",
"action_input": "Your name is Bob."
}
Finished chain.
Got output Your name is Bob.
Entering new agent_executor chain...
```json
{
"action": "search",
"action_input": "weather in pomfret"
}
```
A steady rain early...then remaining cloudy with a few showers. High 48F. Winds WNW at 10 to 15 mph. Chance of rain 80%.
```json
{
"action": "Final Answer",
"action_input": "The weather in Pomfret is a steady rain early...then remaining cloudy with a few showers. High 48F. Winds WNW at 10 to 15 mph. Chance of rain 80%."
}
```
Finished chain.
Got output The weather in Pomfret is a steady rain early...then remaining cloudy with a few showers. High 48F. Winds WNW at 10 to 15 mph. Chance of rain 80%.