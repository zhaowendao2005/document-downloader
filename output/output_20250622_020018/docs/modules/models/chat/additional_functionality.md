---
url: https://js.langchain.com.cn/docs/modules/models/chat/additional_functionality
crawled_at: 2025-06-22T02:00:25.344788
---

附加功能: 聊天模型
我们为聊天模型提供了许多附加功能。在以下示例中，我们将使用
ChatOpenAI
模型。
附加方法
​
L angChain 为与聊天模型交互提供了许多附加方法:
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
;
import
{
HumanChatMessage
,
SystemChatMessage
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
const
chat
=
new
ChatOpenAI
(
{
modelName
:
"gpt-3.5-turbo"
}
)
;
// Pass in a list of messages to `call` to start a conversation. In this simple example, we only pass in one message.
const
responseA
=
await
chat
.
call
(
[
new
HumanChatMessage
(
"What is a good name for a company that makes colorful socks?"
)
,
]
)
;
console
.
log
(
responseA
)
;
// AIChatMessage { text: '\n\nRainbow Sox Co.' }
// You can also pass in multiple messages to start a conversation.
// The first message is a system message that describes the context of the conversation.
// The second message is a human message that starts the conversation.
const
responseB
=
await
chat
.
call
(
[
new
SystemChatMessage
(
"You are a helpful assistant that translates English to French."
)
,
new
HumanChatMessage
(
"Translate: I love programming."
)
,
]
)
;
console
.
log
(
responseB
)
;
// AIChatMessage { text: "J'aime programmer." }
// Similar to LLMs, you can also use `generate` to generate chat completions for multiple sets of messages.
const
responseC
=
await
chat
.
generate
(
[
[
new
SystemChatMessage
(
"You are a helpful assistant that translates English to French."
)
,
new
HumanChatMessage
(
"Translate this sentence from English to French. I love programming."
)
,
]
,
[
new
SystemChatMessage
(
"You are a helpful assistant that translates English to French."
)
,
new
HumanChatMessage
(
"Translate this sentence from English to French. I love artificial intelligence."
)
,
]
,
]
)
;
console
.
log
(
responseC
)
;
/*
{
generations: [
[
{
text: "J'aime programmer.",
message: AIChatMessage { text: "J'aime programmer." },
}
],
[
{
text: "J'aime l'intelligence artificielle.",
message: AIChatMessage { text: "J'aime l'intelligence artificielle." }
}
]
]
}
*/
}
;
流式传输
​
与 LLMs 类似，您可以从聊天模型中流式传输响应。这对于需要实时响应用户输入的聊天机器人非常有用。
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
;
import
{
HumanChatMessage
}
from
"langchain/schema"
;
const
chat
=
new
ChatOpenAI
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
[
new
HumanChatMessage
(
"Tell me a joke."
)
]
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
// { token: '' }
// { token: '\n\n' }
// { token: 'Why' }
// { token: ' don' }
// { token: "'t" }
// { token: ' scientists' }
// { token: ' trust' }
// { token: ' atoms' }
// { token: '?\n\n' }
// { token: 'Because' }
// { token: ' they' }
// { token: ' make' }
// { token: ' up' }
// { token: ' everything' }
// { token: '.' }
// { token: '' }
// AIChatMessage {
//   text: "\n\nWhy don't scientists trust atoms?\n\nBecause they make up everything."
// }
添加超时
​
默认情况下，LangChain 会无限期等待模型提供者的响应。如果您想添加超时，可以在调用模型时传递一个以毫秒为单位的
timeout
选项。例如，对于 OpenAI:
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
;
import
{
HumanChatMessage
}
from
"langchain/schema"
;
const
chat
=
new
ChatOpenAI
(
{
temperature
:
1
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
[
new
HumanChatMessage
(
"What is a good name for a company that makes colorful socks?"
)
,
]
,
{
timeout
:
1000
}
// 1s timeout
)
;
console
.
log
(
response
)
;
// AIChatMessage { text: '\n\nRainbow Sox Co.' }
取消请求
​
您可以在调用模型时通过传递
signal
选项来取消请求。例如，对于 OpenAI:
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
;
import
{
HumanChatMessage
}
from
"langchain/schema"
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
1
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
const
res
=
await
model
.
call
(
[
new
HumanChatMessage
(
"What is a good name for a company that makes colorful socks?"
)
,
]
,
{
signal
:
controller
.
signal
}
)
;
console
.
log
(
res
)
;
/*
'\n\nSocktastic Colors'
*/
注意，只有底层提供程序暴露该选项时，才会取消正在进行的请求。如果可能，LangChain 将取消底层请求，否则将取消响应的处理。
处理速率限制
​
一些提供程序具有速率限制。如果超过速率限制，您将收到错误提示。为帮助您处理这种情况，LangChain 在实例化聊天模型时提供了
maxConcurrency
选项。该选项允许您指定要向提供程序发出的并发请求的最大数量。如果超出此数字，则 LangChain 将自动将您的请求排队，以在之前的请求完成后发送。
例如，如果您设置
maxConcurrency:5
，则LangChain一次仅会向提供程序发送5个请求。如果您发送10个请求，则会立即发送前5个请求，并将下一个5个请求排队。一旦前5个请求中的一个完成，队列中的下一个请求将被发送。
要使用此功能，只需在实例化LLM时传递
maxConcurrency:<number>
即可。例如：
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
;
const
model
=
new
ChatOpenAI
(
{
maxConcurrency
:
5
}
)
;
处理API错误
​
如果模型提供程序从其API返回错误，则默认情况下，LangChain将在指数回退上重试最多6次。这使得错误恢复无需任何额外的努力。如果您想更改此行为，则可以在实例化模型时传递
maxRetries
选项。例如@＃：
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
;
const
model
=
new
ChatOpenAI
(
{
maxRetries
:
10
}
)
;
订阅事件
​
特别是使用代理时，作为聊天模型处理提示时可能会有很多事情来回发生。对于代理，响应对象包含一个intermediateSteps对象，您可以打印以查看它所采取的步骤概述。如果这还不够，您想查看与聊天模型的每个交换，您可以将回调传递给聊天模型以进行自定义日志记录（或任何其他您想要执行的操作)，因为模型通过这些步骤@＃。
有关可用事件的更多信息，请参见文档中的回调（Callbacks）
Callbacks
部分。
import
{
HumanChatMessage
,
LLMResult
}
from
"langchain/schema"
;
import
{
ChatOpenAI
}
from
"langchain/chat_models/openai"
;
// We can pass in a list of CallbackHandlers to the LLM constructor to get callbacks for various events.
const
model
=
new
ChatOpenAI
(
{
callbacks
:
[
{
handleLLMStart
:
async
(
llm
:
{
name
:
string
}
,
prompts
:
string
[
]
)
=>
{
console
.
log
(
JSON
.
stringify
(
llm
,
null
,
2
)
)
;
console
.
log
(
JSON
.
stringify
(
prompts
,
null
,
2
)
)
;
}
,
handleLLMEnd
:
async
(
output
:
LLMResult
)
=>
{
console
.
log
(
JSON
.
stringify
(
output
,
null
,
2
)
)
;
}
,
handleLLMError
:
async
(
err
:
Error
)
=>
{
console
.
error
(
err
)
;
}
,
}
,
]
,
}
)
;
await
model
.
call
(
[
new
HumanChatMessage
(
"What is a good name for a company that makes colorful socks?"
)
,
]
)
;
/*
{
"name": "openai"
}
[
"Human: What is a good name for a company that makes colorful socks?"
]
{
"generations": [
[
{
"text": "Rainbow Soles",
"message": {
"text": "Rainbow Soles"
}
}
]
],
"llmOutput": {
"tokenUsage": {
"completionTokens": 4,
"promptTokens": 21,
"totalTokens": 25
}
}
}
*/