---
url: https://js.langchain.com.cn/docs/production/callbacks/
crawled_at: 2025-06-22T02:00:26.045821
---

事件 / 回调
LangChain 提供了一个回调系统，允许你在 LLM 应用程序的各个阶段中进行钩子处理。这对于记录日志、
监视
、
流媒体
和其他任务非常有用。
你可以通过 API 中使用的
callbacks
参数来订阅这些事件。此方法接受一个处理程序对象的列表，这些对象应该实现
API 文档
中描述的一个或多个方法。
深入了解
​
📄️
创建回调处理程序
创建自定义处理程序
📄️
自定义Chains中的回调
LangChain旨在可扩展。 您可以将自己的自定义Chains和Agents添加到库中。 本页将向您展示如何将回调添加到自定义的Chains和Agents中。
如何使用回调
​
在 API 中的大多数对象上（
Chains
、
Models
、
Tools
、
Agents
等)都提供了
callbacks
参数，它有两个不同的用法:
构造器回调
​
在构造函数中定义，如
new LLMChain({ callbacks: [handler] })
，将用于该对象上进行的所有调用，并且仅适用于该对象本身。例如，如果你将处理程序传递给
LLMChain
构造函数，则不会被连接到该链上的模型使用。
import
{
ConsoleCallbackHandler
}
from
"langchain/callbacks"
;
import
{
OpenAI
}
from
"langchain/llms/openai"
;
const
llm
=
new
OpenAI
(
{
temperature
:
0
,
// This handler will be used for all calls made with this LLM.
callbacks
:
[
new
ConsoleCallbackHandler
(
)
]
,
}
)
;
请求回调
​
在发出请求的
call()
/
run()
/
apply()
方法中定义，例如
chain.call({ input: '...' }， [handler])
，将仅用于该特定请求及其包含的所有子请求（例如，对 LLMChain 的调用会触发对模型的调用，该模型使用在
call()
方法中传递的相同处理程序)。
import
{
ConsoleCallbackHandler
}
from
"langchain/callbacks"
;
import
{
OpenAI
}
from
"langchain/llms/openai"
;
const
llm
=
new
OpenAI
(
{
temperature
:
0
,
}
)
;
// This handler will be used only for this call.
const
response
=
await
llm
.
call
(
"1 + 1 ="
,
undefined
,
[
new
ConsoleCallbackHandler
(
)
,
]
)
;
详细模式
​
verbose
参数可用于API中的大部分对象（链接，模型，工具，代理等)作为构造参数。例如，
new LLMChain({ verbose: true })
，它相当于将
callbacks
参数传递给该对象和所有子对象的
ConsoleCallbackHandler
。这对于调试非常有用，因为它会将所有事件记录在控制台上。您还可以通过设置环境变量
LANGCHAIN_VERBOSE=true
来为整个应用程序启用详细模式。
import
{
PromptTemplate
}
from
"langchain/prompts"
;
import
{
LLMChain
}
from
"langchain/chains"
;
import
{
OpenAI
}
from
"langchain/llms/openai"
;
const
chain
=
new
LLMChain
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
prompt
:
PromptTemplate
.
fromTemplate
(
"Hello, world!"
)
,
// This will enable logging of all Chain *and* LLM events to the console.
verbose
:
true
,
}
)
;
你何时需要使用它们？
​
构造函数回调最适用于诸如日志记录，监视等用例，这些用例不特定于单个请求，而是适用于整个链。例如，如果您要记录所有发送到LLMChain的请求，则应将处理程序传递给构造函数。
请求回调最适用于流式传输等用例，其中您需要将单个请求的输出流到特定的websocket连接或其他类似的用例。例如，如果您想将单个请求的输出流到websocket，则应将处理程序传递给
call()
方法。
使用示例
​
内置处理程序
​
LangChain提供了一些内置处理程序，可用于入门。这些可在
langchain/callbacks
模块中使用。最基本的处理程序是
ConsoleCallbackHandler
，只需将所有事件记录到控制台即可。在将
verbose
标志设置为
true
的情况下，
ConsoleCallbackHandler
将在不显式传递的情况下被调用。
import
{
ConsoleCallbackHandler
}
from
"langchain/callbacks"
;
import
{
LLMChain
}
from
"langchain/chains"
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
PromptTemplate
}
from
"langchain/prompts"
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
handler
=
new
ConsoleCallbackHandler
(
)
;
const
llm
=
new
OpenAI
(
{
temperature
:
0
,
callbacks
:
[
handler
]
}
)
;
const
prompt
=
PromptTemplate
.
fromTemplate
(
"1 + {number} ="
)
;
const
chain
=
new
LLMChain
(
{
prompt
,
llm
,
callbacks
:
[
handler
]
}
)
;
const
output
=
await
chain
.
call
(
{
number
:
2
}
)
;
/*
Entering new llm_chain chain...
Finished chain.
*/
console
.
log
(
output
)
;
/*
{ text: ' 3\n\n3 - 1 = 2' }
*/
// The non-enumerable key `__run` contains the runId.
console
.
log
(
output
.
__run
)
;
/*
{ runId: '90e1f42c-7cb4-484c-bf7a-70b73ef8e64b' }
*/
}
;
One-off handlers
​
您可以通过将普通对象传递给
callbacks
参数来创建一个临时处理程序。该对象应实现
CallbackHandlerMethods
接口。如果您需要创建一个仅用于单个请求的处理程序，这将非常有用，例如流式传输LLM / Agent /等的输出到WebSocket。
import
{
OpenAI
}
from
"langchain/llms/openai"
;
// To enable streaming, we pass in `streaming: true` to the LLM constructor.
// Additionally, we pass in a handler for the `handleLLMNewToken` event.
const
chat
=
new
OpenAI
(
{
maxTokens
:
25
,
streaming
:
true
,
}
)
;
const
response
=
await
chat
.
call
(
"Tell me a joke."
,
undefined
,
[
{
handleLLMNewToken
(
token
:
string
)
{
console
.
log
(
{
token
}
)
;
}
,
}
,
]
)
;
console
.
log
(
response
)
;
/*
{ token: '\n' }
{ token: '\n' }
{ token: 'Q' }
{ token: ':' }
{ token: ' Why' }
{ token: ' did' }
{ token: ' the' }
{ token: ' chicken' }
{ token: ' cross' }
{ token: ' the' }
{ token: ' playground' }
{ token: '?' }
{ token: '\n' }
{ token: 'A' }
{ token: ':' }
{ token: ' To' }
{ token: ' get' }
{ token: ' to' }
{ token: ' the' }
{ token: ' other' }
{ token: ' slide' }
{ token: '.' }
Q: Why did the chicken cross the playground?
A: To get to the other slide.
*/
多个处理程序
​
我们在
CallbackManager
类上提供了一种方法，允许您创建一个临时处理程序。如果您需要创建一个仅用于单个请求的处理程序，这将非常有用，例如流式传输LLM / Agent /等的输出到WebSocket。
This is a more complete example that passes a
CallbackManager
to a ChatModel, and LLMChain, a Tool, and an Agent.
import
{
LLMChain
}
from
"langchain/chains"
;
import
{
AgentExecutor
,
ZeroShotAgent
}
from
"langchain/agents"
;
import
{
BaseCallbackHandler
}
from
"langchain/callbacks"
;
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
;
import
{
Calculator
}
from
"langchain/tools/calculator"
;
import
{
AgentAction
}
from
"langchain/schema"
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
// You can implement your own callback handler by extending BaseCallbackHandler
class
CustomHandler
extends
BaseCallbackHandler
{
name
=
"custom_handler"
;
handleLLMNewToken
(
token
:
string
)
{
console
.
log
(
"token"
,
{
token
}
)
;
}
handleLLMStart
(
llm
:
{
name
:
string
}
,
_prompts
:
string
[
]
)
{
console
.
log
(
"handleLLMStart"
,
{
llm
}
)
;
}
handleChainStart
(
chain
:
{
name
:
string
}
)
{
console
.
log
(
"handleChainStart"
,
{
chain
}
)
;
}
handleAgentAction
(
action
:
AgentAction
)
{
console
.
log
(
"handleAgentAction"
,
action
)
;
}
handleToolStart
(
tool
:
{
name
:
string
}
)
{
console
.
log
(
"handleToolStart"
,
{
tool
}
)
;
}
}
const
handler1
=
new
CustomHandler
(
)
;
// Additionally, you can use the `fromMethods` method to create a callback handler
const
handler2
=
BaseCallbackHandler
.
fromMethods
(
{
handleLLMStart
(
llm
,
_prompts
:
string
[
]
)
{
console
.
log
(
"handleLLMStart: I'm the second handler!!"
,
{
llm
}
)
;
}
,
handleChainStart
(
chain
)
{
console
.
log
(
"handleChainStart: I'm the second handler!!"
,
{
chain
}
)
;
}
,
handleAgentAction
(
action
)
{
console
.
log
(
"handleAgentAction"
,
action
)
;
}
,
handleToolStart
(
tool
)
{
console
.
log
(
"handleToolStart"
,
{
tool
}
)
;
}
,
}
)
;
// You can restrict callbacks to a particular object by passing it upon creation
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
,
callbacks
:
[
handler2
]
,
// this will issue handler2 callbacks related to this model
streaming
:
true
,
// needed to enable streaming, which enables handleLLMNewToken
}
)
;
const
tools
=
[
new
Calculator
(
)
]
;
const
agentPrompt
=
ZeroShotAgent
.
createPrompt
(
tools
)
;
const
llmChain
=
new
LLMChain
(
{
llm
:
model
,
prompt
:
agentPrompt
,
callbacks
:
[
handler2
]
,
// this will issue handler2 callbacks related to this chain
}
)
;
const
agent
=
new
ZeroShotAgent
(
{
llmChain
,
allowedTools
:
[
"search"
]
,
}
)
;
const
agentExecutor
=
AgentExecutor
.
fromAgentAndTools
(
{
agent
,
tools
,
}
)
;
/*
* When we pass the callback handler to the agent executor, it will be used for all
* callbacks related to the agent and all the objects involved in the agent's
* execution, in this case, the Tool, LLMChain, and LLM.
*
* The `handler2` callback handler will only be used for callbacks related to the
* LLMChain and LLM, since we passed it to the LLMChain and LLM objects upon creation.
*/
const
result
=
await
agentExecutor
.
call
(
{
input
:
"What is 2 to the power of 8"
,
}
,
[
handler1
]
)
;
// this is needed to see handleAgentAction
/*
handleChainStart { chain: { name: 'agent_executor' } }
handleChainStart { chain: { name: 'llm_chain' } }
handleChainStart: I'm the second handler!! { chain: { name: 'llm_chain' } }
handleLLMStart { llm: { name: 'openai' } }
handleLLMStart: I'm the second handler!! { llm: { name: 'openai' } }
token { token: '' }
token { token: 'I' }
token { token: ' can' }
token { token: ' use' }
token { token: ' the' }
token { token: ' calculator' }
token { token: ' tool' }
token { token: ' to' }
token { token: ' solve' }
token { token: ' this' }
token { token: '.\n' }
token { token: 'Action' }
token { token: ':' }
token { token: ' calculator' }
token { token: '\n' }
token { token: 'Action' }
token { token: ' Input' }
token { token: ':' }
token { token: ' ' }
token { token: '2' }
token { token: '^' }
token { token: '8' }
token { token: '' }
handleAgentAction {
tool: 'calculator',
toolInput: '2^8',
log: 'I can use the calculator tool to solve this.\n' +
'Action: calculator\n' +
'Action Input: 2^8'
}
handleToolStart { tool: { name: 'calculator' } }
handleChainStart { chain: { name: 'llm_chain' } }
handleChainStart: I'm the second handler!! { chain: { name: 'llm_chain' } }
handleLLMStart { llm: { name: 'openai' } }
handleLLMStart: I'm the second handler!! { llm: { name: 'openai' } }
token { token: '' }
token { token: 'That' }
token { token: ' was' }
token { token: ' easy' }
token { token: '!\n' }
token { token: 'Final' }
token { token: ' Answer' }
token { token: ':' }
token { token: ' ' }
token { token: '256' }
token { token: '' }
*/
console
.
log
(
result
)
;
/*
{
output: '256',
__run: { runId: '26d481a6-4410-4f39-b74d-f9a4f572379a' }
}
*/
}
;