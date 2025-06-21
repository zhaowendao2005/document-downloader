---
url: https://js.langchain.com.cn/docs/modules/models/llms/additional_functionality
crawled_at: 2025-06-22T02:00:25.590829
---

LLMs: 附加功能
我们为LLM提供了许多附加功能。在下面的大多数示例中，我们将使用
OpenAI
LLM。然而，所有这些功能都适用于所有LLMs。
附加方法
​
LangChain为与LLMs交互提供了许多附加方法:
import
{
OpenAI
}
from
"langchain/llms/openai"
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
modelA
=
new
OpenAI
(
)
;
// `call` is a simple string-in, string-out method for interacting with the model.
const
resA
=
await
modelA
.
call
(
"What would be a good company name a company that makes colorful socks?"
)
;
console
.
log
(
{
resA
}
)
;
// { resA: '\n\nSocktastic Colors' }
// `generate` allows you to generate multiple completions for multiple prompts (in a single request for some models).
const
resB
=
await
modelA
.
generate
(
[
"What would be a good company name a company that makes colorful socks?"
,
"What would be a good company name a company that makes colorful sweaters?"
,
]
)
;
// `resB` is a `LLMResult` object with a `generations` field and `llmOutput` field.
// `generations` is a `Generation[][]`, each `Generation` having a `text` field.
// Each input to the LLM could have multiple generations (depending on the `n` parameter), hence the list of lists.
console
.
log
(
JSON
.
stringify
(
resB
,
null
,
2
)
)
;
/*
{
"generations": [
[{
"text": "\n\nVibrant Socks Co.",
"generationInfo": {
"finishReason": "stop",
"logprobs": null
}
}],
[{
"text": "\n\nRainbow Knitworks.",
"generationInfo": {
"finishReason": "stop",
"logprobs": null
}
}]
],
"llmOutput": {
"tokenUsage": {
"completionTokens": 17,
"promptTokens": 29,
"totalTokens": 46
}
}
}
*/
// We can specify additional parameters the specific model provider supports, like `temperature`:
const
modelB
=
new
OpenAI
(
{
temperature
:
0.9
}
)
;
const
resC
=
await
modelA
.
call
(
"What would be a good company name a company that makes colorful socks?"
)
;
console
.
log
(
{
resC
}
)
;
// { resC: '\n\nKaleidoSox' }
// We can get the number of tokens for a given input for a specific model.
const
numTokens
=
modelB
.
getNumTokens
(
"How many tokens are in this input?"
)
;
console
.
log
(
{
numTokens
}
)
;
// { numTokens: 8 }
}
;
流式响应
​
某些LLMs提供流式响应。这意味着您可以在整个响应被返回之前开始处理它。这很有用，如果您想要在生成响应时向用户显示响应，或者如果你要处理正在生成的响应。
LangChain目前提供
OpenAI
LLM的流式传输:
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
缓存
​
LangChain为LLMs提供可选的缓存层。有两个原因很有用:
如果你经常请求相同的完成多次，它可以通过减少你对LLM提供商的调用次数来节省您的费用。
它可以通过减少你对LLM提供商的API调用次数来加速你的应用程序。
内存中的缓存
​
默认缓存存储在内存中。这意味着如果重新启动应用程序，则会清除缓存。
你可以在实例化LLM时传递
cache: true
来启用它。例如:
import
{
OpenAI
}
from
"langchain/llms/openai"
;
const
model
=
new
OpenAI
(
{
cache
:
true
}
)
;
使用Momento进行缓存
​
LangChain还提供了基于Momento的缓存。
Momento
是一种分布式的服务器端无服务器缓存，不需要任何设置或基础设施维护。要使用它，您需要安装
@gomomento/sdk
软件包:
npm
Yarn
pnpm
npm
install
@gomomento/sdk
yarn
add
@gomomento/sdk
pnpm
add
@gomomento/sdk
接下来，您需要注册并创建API密钥。完成后，像这样实例化LLM时传递一个
cache
选项:
Next you'll need to sign up and create an API key. Once you've done that, pass a
cache
option when you instantiate the LLM like this:
import
{
OpenAI
}
from
"langchain/llms/openai"
;
import
{
MomentoCache
}
from
"langchain/cache/momento"
;
import
{
CacheClient
,
Configurations
,
CredentialProvider
,
}
from
"@gomomento/sdk"
;
// See https://github.com/momentohq/client-sdk-javascript for connection options
const
client
=
new
CacheClient
(
{
configuration
:
Configurations
.
Laptop
.
v1
(
)
,
credentialProvider
:
CredentialProvider
.
fromEnvironmentVariable
(
{
environmentVariableName
:
"MOMENTO_AUTH_TOKEN"
,
}
)
,
defaultTtlSeconds
:
60
*
60
*
24
,
}
)
;
const
cache
=
await
MomentoCache
.
fromProps
(
{
client
,
cacheName
:
"langchain"
,
}
)
;
const
model
=
new
OpenAI
(
{
cache
}
)
;
###使用Redis进行缓存
LangChain还提供了基于Redis的缓存。如果您想要在多个进程或服务器之间共享缓存，这将非常有用。要使用它，您需要安装
redis
软件包:
npm
Yarn
pnpm
npm
install
redis
yarn
add
redis
pnpm
add
redis
然后，当您实例化LLM时，可以通过传递一个
cache
选项来使用它。例如:
import
{
OpenAI
}
from
"langchain/llms/openai"
;
import
{
RedisCache
}
from
"langchain/cache/redis"
;
import
{
createClient
}
from
"redis"
;
// See https://github.com/redis/node-redis for connection options
const
client
=
createClient
(
)
;
const
cache
=
new
RedisCache
(
client
)
;
const
model
=
new
OpenAI
(
{
cache
}
)
;
##添加超时
Adding a timeout
​
默认情况下，LangChain将无限期地等待模型提供程序的响应。如果要添加超时，您可以在调用模型时传递一个以毫秒为单位的
timeout
选项。例如，对于OpenAI:
import
{
OpenAI
}
from
"langchain/llms/openai"
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
1
}
)
;
const
resA
=
await
model
.
call
(
"What would be a good company name a company that makes colorful socks?"
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
{
resA
}
)
;
// '\n\nSocktastic Colors' }
取消请求
​
您可以在调用模型时传递一个
signal
选项来取消请求。例如，对于OpenAI:
import
{
OpenAI
}
from
"langchain/llms/openai"
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
"What would be a good company name a company that makes colorful socks?"
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
请注意，如果底层提供程序公开了取消请求的选项，那么此操作仅会取消即将发出的请求。LangChain 将尽可能取消底层请求，否则它将取消响应的处理。
Dealing with Rate Limits
​
一些LLM提供商有速率限制。如果您超过了速率限制，将会出现错误。为了帮助您应对这个问题，LangChain在实例化LLM时提供了“maxConcurrency”选项。该选项允许您指定要发送到LLM提供商的最大并发请求数。如果您超过了这个数字，LangChain会自动将您的请求排队，以在先前的请求完成后发送。
例如，如果您设置
maxConcurrency: 5
，那么LangChain每次只会向LLM提供商发送5个请求。如果您发送了10个请求，前5个将会立即发送，而后5个将会排队等待。一旦前5个请求中的一个完成了，队列中的下一个请求将会发送。
要使用此功能，只需在实例化LLM时传递
maxConcurrency:<数字>
。例如:
import
{
OpenAI
}
from
"langchain/llms/openai"
;
const
model
=
new
OpenAI
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
如果模型提供商从其API返回错误，默认情况下，LangChain将在指数回退上最多重试6次。这样可以实现错误恢复，而无需任何额外的努力。如果您想更改此行为，可以在实例化模型时传递
maxRetries
选项。例如:
import
{
OpenAI
}
from
"langchain/llms/openai"
;
const
model
=
new
OpenAI
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
特别是在使用代理时，在 LLM 处理提示时可能会有大量的后台交互。对于代理，响应对象包含一个
intermediateSteps
对象，您可以打印该对象来查看它所采取的步骤概述。如果这不够用，并且您想要看到与 LLM 的每个交互，您可以将回调传递给 LLM，以进行自定义日志记录（或任何其他您想要执行的操作），当模型通过这些步骤时。
如需了解可用事件的更多信息，请参阅文档中的
[回调]
部分(/docs/production/callbacks/)。#Callbacks
import
{
LLMResult
}
from
"langchain/schema"
;
import
{
OpenAI
}
from
"langchain/llms/openai"
;
// We can pass in a list of CallbackHandlers to the LLM constructor to get callbacks for various events.
const
model
=
new
OpenAI
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
"What would be a good company name a company that makes colorful socks?"
)
;
// {
//     "name": "openai"
// }
// [
//     "What would be a good company name a company that makes colorful socks?"
// ]
// {
//   "generations": [
//     [
//         {
//             "text": "\n\nSocktastic Splashes.",
//             "generationInfo": {
//                 "finishReason": "stop",
//                 "logprobs": null
//             }
//         }
//     ]
//  ],
//   "llmOutput": {
//     "tokenUsage": {
//         "completionTokens": 9,
//          "promptTokens": 14,
//          "totalTokens": 23
//     }
//   }
// }