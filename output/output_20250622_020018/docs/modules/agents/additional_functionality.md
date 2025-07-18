---
url: https://js.langchain.com.cn/docs/modules/agents/additional_functionality
crawled_at: 2025-06-22T02:00:19.942276
---

Agents的其他功能
我们为Agents提供了许多其他功能。您还应查看
LLM-specific features
和
Chat Model-specific features
。
添加超时
​
默认情况下，LangChain将无限期等待模型提供者的响应。如果您想添加超时，可以在运行代理时传递以毫秒为单位的“timeout”选项。例如
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
}
)
;
try
{
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
,
timeout
:
2000
}
)
;
// 2 seconds
}
catch
(
e
)
{
console
.
log
(
e
)
;
/*
Error: Cancel: canceled
at file:///Users/nuno/dev/langchainjs/langchain/dist/util/async_caller.js:60:23
at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
at RetryOperation._fn (/Users/nuno/dev/langchainjs/node_modules/p-retry/index.js:50:12) {
attemptNumber: 1,
retriesLeft: 6
}
*/
}
取消请求
​
您可以通过在运行代理时传递“signal”选项来取消请求。例如
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
}
)
;
const
controller
=
new
AbortController
(
)
;
// Call `controller.abort()` somewhere to cancel the request.
setTimeout
(
(
)
=>
{
controller
.
abort
(
)
;
}
,
2000
)
;
try
{
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
,
signal
:
controller
.
signal
}
)
;
}
catch
(
e
)
{
console
.
log
(
e
)
;
/*
Error: Cancel: canceled
at file:///Users/nuno/dev/langchainjs/langchain/dist/util/async_caller.js:60:23
at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
at RetryOperation._fn (/Users/nuno/dev/langchainjs/node_modules/p-retry/index.js:50:12) {
attemptNumber: 1,
retriesLeft: 6
}
*/
}
注意：如果底层提供程序公开该选项，这将仅取消传出请求。如果可能，LangChain将取消底层请求，否则它将取消响应的处理。
订阅事件
​
您可以订阅代理和基础工具链和模型发出的许多事件。
有关可用事件的更多信息，请参见文档中的
Callbacks
部分。
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
run
(
input
,
[
{
handleAgentAction
(
action
,
runId
)
{
console
.
log
(
"\nhandleAgentAction"
,
action
,
runId
)
;
}
,
handleAgentEnd
(
action
,
runId
)
{
console
.
log
(
"\nhandleAgentEnd"
,
action
,
runId
)
;
}
,
handleToolEnd
(
output
,
runId
)
{
console
.
log
(
"\nhandleToolEnd"
,
output
,
runId
)
;
}
,
}
,
]
)
;
/*
handleAgentAction {
tool: 'search',
toolInput: 'Olivia Wilde boyfriend',
log: " I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.\n" +
'Action: search\n' +
'Action Input: "Olivia Wilde boyfriend"'
} 9b978461-1f6f-4d5f-80cf-5b229ce181b6
handleToolEnd In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling. Their relationship ended in November 2022. 062fef47-8ad1-4729-9949-a57be252e002
handleAgentAction {
tool: 'search',
toolInput: 'Harry Styles age',
log: " I need to find out Harry Styles' age.\n" +
'Action: search\n' +
'Action Input: "Harry Styles age"'
} 9b978461-1f6f-4d5f-80cf-5b229ce181b6
handleToolEnd 29 years 9ec91e41-2fbf-4de0-85b6-12b3e6b3784e 61d77e10-c119-435d-a985-1f9d45f0ef08
handleAgentAction {
tool: 'calculator',
toolInput: '29^0.23',
log: ' I need to calculate 29 raised to the 0.23 power.\n' +
'Action: calculator\n' +
'Action Input: 29^0.23'
} 9b978461-1f6f-4d5f-80cf-5b229ce181b6
handleToolEnd 2.169459462491557 07aec96a-ce19-4425-b863-2eae39db8199
handleAgentEnd {
returnValues: {
output: "Harry Styles is Olivia Wilde's boyfriend and his current age raised to the 0.23 power is 2.169459462491557."
},
log: ' I now know the final answer.\n' +
"Final Answer: Harry Styles is Olivia Wilde's boyfriend and his current age raised to the 0.23 power is 2.169459462491557."
} 9b978461-1f6f-4d5f-80cf-5b229ce181b6
*/
console
.
log
(
{
result
}
)
;
// { result: "Harry Styles is Olivia Wilde's boyfriend and his current age raised to the 0.23 power is 2.169459462491557." }
日志记录和跟踪
​
您可以在创建代理时传递“verbose”标志，以启用将所有事件记录到控制台的日志记录。例如
您还可以通过将LANGCHAIN_TRACING环境变量设置为“true”来启用
跟踪
。
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
[chain/start] [1:chain:agent_executor] Entering Chain run with input: {
"input": "Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?"
}
[chain/start] [1:chain:agent_executor > 2:chain:llm_chain] Entering Chain run with input: {
"input": "Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?",
"agent_scratchpad": "",
"stop": [
"Observation: "
]
}
[llm/start] [1:chain:agent_executor > 2:chain:llm_chain > 3:llm:openai] Entering LLM run with input: {
"prompts": [
"Answer the following questions as best you can. You have access to the following tools:search: a search engine. useful for when you need to answer questions about current events. input should be a search query.calculator: Useful for getting the result of a math expression. The input to this tool should be a valid mathematical expression that could be executed by a simple calculator.Use the following format in your response:Question: the input question you must answerThought: you should always think about what to doAction: the action to take, should be one of [search,calculator]Action Input: the input to the actionObservation: the result of the action... (this Thought/Action/Action Input/Observation can repeat N times)Thought: I now know the final answerFinal Answer: the final answer to the original input questionBegin!Question: Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?Thought:"
]
}
[llm/end] [1:chain:agent_executor > 2:chain:llm_chain > 3:llm:openai] [3.52s] Exiting LLM run with output: {
"generations": [
[
{
"text": " I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend"",
"generationInfo": {
"finishReason": "stop",
"logprobs": null
}
}
]
],
"llmOutput": {
"tokenUsage": {
"completionTokens": 39,
"promptTokens": 220,
"totalTokens": 259
}
}
}
[chain/end] [1:chain:agent_executor > 2:chain:llm_chain] [3.53s] Exiting Chain run with output: {
"text": " I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend""
}
[agent/action] [1:chain:agent_executor] Agent selected action: {
"tool": "search",
"toolInput": "Olivia Wilde boyfriend",
"log": " I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend""
}
[tool/start] [1:chain:agent_executor > 4:tool:search] Entering Tool run with input: "Olivia Wilde boyfriend"
[tool/end] [1:chain:agent_executor > 4:tool:search] [845ms] Exiting Tool run with output: "In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling. Their relationship ended in November 2022."
[chain/start] [1:chain:agent_executor > 5:chain:llm_chain] Entering Chain run with input: {
"input": "Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?",
"agent_scratchpad": " I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend"Observation: In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling. Their relationship ended in November 2022.Thought:",
"stop": [
"Observation: "
]
}
[llm/start] [1:chain:agent_executor > 5:chain:llm_chain > 6:llm:openai] Entering LLM run with input: {
"prompts": [
"Answer the following questions as best you can. You have access to the following tools:search: a search engine. useful for when you need to answer questions about current events. input should be a search query.calculator: Useful for getting the result of a math expression. The input to this tool should be a valid mathematical expression that could be executed by a simple calculator.Use the following format in your response:Question: the input question you must answerThought: you should always think about what to doAction: the action to take, should be one of [search,calculator]Action Input: the input to the actionObservation: the result of the action... (this Thought/Action/Action Input/Observation can repeat N times)Thought: I now know the final answerFinal Answer: the final answer to the original input questionBegin!Question: Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?Thought: I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend"Observation: In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling. Their relationship ended in November 2022.Thought:"
]
}
[llm/end] [1:chain:agent_executor > 5:chain:llm_chain > 6:llm:openai] [3.65s] Exiting LLM run with output: {
"generations": [
[
{
"text": " I need to find out Harry Styles' age.Action: searchAction Input: "Harry Styles age"",
"generationInfo": {
"finishReason": "stop",
"logprobs": null
}
}
]
],
"llmOutput": {
"tokenUsage": {
"completionTokens": 23,
"promptTokens": 296,
"totalTokens": 319
}
}
}
[chain/end] [1:chain:agent_executor > 5:chain:llm_chain] [3.65s] Exiting Chain run with output: {
"text": " I need to find out Harry Styles' age.Action: searchAction Input: "Harry Styles age""
}
[agent/action] [1:chain:agent_executor] Agent selected action: {
"tool": "search",
"toolInput": "Harry Styles age",
"log": " I need to find out Harry Styles' age.Action: searchAction Input: "Harry Styles age""
}
[tool/start] [1:chain:agent_executor > 7:tool:search] Entering Tool run with input: "Harry Styles age"
[tool/end] [1:chain:agent_executor > 7:tool:search] [632ms] Exiting Tool run with output: "29 years"
[chain/start] [1:chain:agent_executor > 8:chain:llm_chain] Entering Chain run with input: {
"input": "Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?",
"agent_scratchpad": " I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend"Observation: In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling. Their relationship ended in November 2022.Thought: I need to find out Harry Styles' age.Action: searchAction Input: "Harry Styles age"Observation: 29 yearsThought:",
"stop": [
"Observation: "
]
}
[llm/start] [1:chain:agent_executor > 8:chain:llm_chain > 9:llm:openai] Entering LLM run with input: {
"prompts": [
"Answer the following questions as best you can. You have access to the following tools:search: a search engine. useful for when you need to answer questions about current events. input should be a search query.calculator: Useful for getting the result of a math expression. The input to this tool should be a valid mathematical expression that could be executed by a simple calculator.Use the following format in your response:Question: the input question you must answerThought: you should always think about what to doAction: the action to take, should be one of [search,calculator]Action Input: the input to the actionObservation: the result of the action... (this Thought/Action/Action Input/Observation can repeat N times)Thought: I now know the final answerFinal Answer: the final answer to the original input questionBegin!Question: Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?Thought: I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend"Observation: In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling. Their relationship ended in November 2022.Thought: I need to find out Harry Styles' age.Action: searchAction Input: "Harry Styles age"Observation: 29 yearsThought:"
]
}
[llm/end] [1:chain:agent_executor > 8:chain:llm_chain > 9:llm:openai] [2.72s] Exiting LLM run with output: {
"generations": [
[
{
"text": " I need to calculate 29 raised to the 0.23 power.Action: calculatorAction Input: 29^0.23",
"generationInfo": {
"finishReason": "stop",
"logprobs": null
}
}
]
],
"llmOutput": {
"tokenUsage": {
"completionTokens": 26,
"promptTokens": 329,
"totalTokens": 355
}
}
}
[chain/end] [1:chain:agent_executor > 8:chain:llm_chain] [2.72s] Exiting Chain run with output: {
"text": " I need to calculate 29 raised to the 0.23 power.Action: calculatorAction Input: 29^0.23"
}
[agent/action] [1:chain:agent_executor] Agent selected action: {
"tool": "calculator",
"toolInput": "29^0.23",
"log": " I need to calculate 29 raised to the 0.23 power.Action: calculatorAction Input: 29^0.23"
}
[tool/start] [1:chain:agent_executor > 10:tool:calculator] Entering Tool run with input: "29^0.23"
[tool/end] [1:chain:agent_executor > 10:tool:calculator] [3ms] Exiting Tool run with output: "2.169459462491557"
[chain/start] [1:chain:agent_executor > 11:chain:llm_chain] Entering Chain run with input: {
"input": "Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?",
"agent_scratchpad": " I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend"Observation: In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling. Their relationship ended in November 2022.Thought: I need to find out Harry Styles' age.Action: searchAction Input: "Harry Styles age"Observation: 29 yearsThought: I need to calculate 29 raised to the 0.23 power.Action: calculatorAction Input: 29^0.23Observation: 2.169459462491557Thought:",
"stop": [
"Observation: "
]
}
[llm/start] [1:chain:agent_executor > 11:chain:llm_chain > 12:llm:openai] Entering LLM run with input: {
"prompts": [
"Answer the following questions as best you can. You have access to the following tools:search: a search engine. useful for when you need to answer questions about current events. input should be a search query.calculator: Useful for getting the result of a math expression. The input to this tool should be a valid mathematical expression that could be executed by a simple calculator.Use the following format in your response:Question: the input question you must answerThought: you should always think about what to doAction: the action to take, should be one of [search,calculator]Action Input: the input to the actionObservation: the result of the action... (this Thought/Action/Action Input/Observation can repeat N times)Thought: I now know the final answerFinal Answer: the final answer to the original input questionBegin!Question: Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?Thought: I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.Action: searchAction Input: "Olivia Wilde boyfriend"Observation: In January 2021, Wilde began dating singer Harry Styles after meeting during the filming of Don't Worry Darling. Their relationship ended in November 2022.Thought: I need to find out Harry Styles' age.Action: searchAction Input: "Harry Styles age"Observation: 29 yearsThought: I need to calculate 29 raised to the 0.23 power.Action: calculatorAction Input: 29^0.23Observation: 2.169459462491557Thought:"
]
}
[llm/end] [1:chain:agent_executor > 11:chain:llm_chain > 12:llm:openai] [3.51s] Exiting LLM run with output: {
"generations": [
[
{
"text": " I now know the final answer.Final Answer: Harry Styles is Olivia Wilde's boyfriend and his current age raised to the 0.23 power is 2.169459462491557.",
"generationInfo": {
"finishReason": "stop",
"logprobs": null
}
}
]
],
"llmOutput": {
"tokenUsage": {
"completionTokens": 39,
"promptTokens": 371,
"totalTokens": 410
}
}
}
[chain/end] [1:chain:agent_executor > 11:chain:llm_chain] [3.51s] Exiting Chain run with output: {
"text": " I now know the final answer.Final Answer: Harry Styles is Olivia Wilde's boyfriend and his current age raised to the 0.23 power is 2.169459462491557."
}
[chain/end] [1:chain:agent_executor] [14.90s] Exiting Chain run with output: {
"output": "Harry Styles is Olivia Wilde's boyfriend and his current age raised to the 0.23 power is 2.169459462491557."
}