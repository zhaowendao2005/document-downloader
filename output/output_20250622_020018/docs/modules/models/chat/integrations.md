---
url: https://js.langchain.com.cn/docs/modules/models/chat/integrations
crawled_at: 2025-06-22T02:00:25.393847
---

集成: 聊天模型
LangChain提供了许多与不同模型提供者集成的聊天模型实现。它们如下所示:
ChatOpenAI
（聊天OpenAI)
​
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
temperature
:
0.9
,
openAIApiKey
:
"YOUR-API-KEY"
,
// In Node.js defaults to process.env.OPENAI_API_KEY
}
)
;
Azure
ChatOpenAI
（Azure的聊天OpenAI)
​
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
temperature
:
0.9
,
azureOpenAIApiKey
:
"YOUR-API-KEY"
,
// In Node.js defaults to process.env.AZURE_OPENAI_API_KEY
azureOpenAIApiInstanceName
:
"YOUR-INSTANCE-NAME"
,
// In Node.js defaults to process.env.AZURE_OPENAI_API_INSTANCE_NAME
azureOpenAIApiDeploymentName
:
"YOUR-DEPLOYMENT-NAME"
,
// In Node.js defaults to process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME
azureOpenAIApiVersion
:
"YOUR-API-VERSION"
,
// In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION
}
)
;
ChatAnthropic
（聊天Anthropic)
​
import
{
ChatAnthropic
}
from
"langchain/chat_models/anthropic"
;
const
model
=
new
ChatAnthropic
(
{
temperature
:
0.9
,
apiKey
:
"YOUR-API-KEY"
,
// In Node.js defaults to process.env.ANTHROPIC_API_KEY
}
)
;
PromptLayerChatOpenAI
（Prompt Layer聊天OpenAI)
​
可以传入可选的
returnPromptLayerId
布尔值来获取像下面这样的
promptLayerRequestId
。下面是一个获取 PromptLayerChatOpenAI 请求ID 的示例:
import
{
PromptLayerChatOpenAI
}
from
"langchain/chat_models/openai"
;
const
chat
=
new
PromptLayerChatOpenAI
(
{
returnPromptLayerId
:
true
,
}
)
;
const
respA
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
]
,
]
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
respA
,
null
,
3
)
)
;
/*
{
"generations": [
[
{
"text": "Bonjour! Je suis un assistant utile qui peut vous aider à traduire de l'anglais vers le français. Que puis-je faire pour vous aujourd'hui?",
"message": {
"type": "ai",
"data": {
"content": "Bonjour! Je suis un assistant utile qui peut vous aider à traduire de l'anglais vers le français. Que puis-je faire pour vous aujourd'hui?"
}
},
"generationInfo": {
"promptLayerRequestId": 2300682
}
}
]
],
"llmOutput": {
"tokenUsage": {
"completionTokens": 35,
"promptTokens": 19,
"totalTokens": 54
}
}
}
*/
Google Vertex AI
（Google 顶点AI)
​
Vertex AI 实现旨在在 Node.js 中使用，而不是直接从浏览器中使用，因为需要使用服务帐户才能使用。
在运行此代码之前，您应该确保已为相关项目启用了 Vertex AI API，并且已经使用以下方法之一进行了 Google Cloud 身份验证:
您已登录帐户（使用
gcloud auth application-default login
）进入 Google Cloud。
您正在运行于允许服务账户所在的机器上。
您已下载服务账户凭证，可以使用该服务账户访问该项目。
您已下载了允许访问该项目的服务账号的凭证，并将
GOOGLE_APPLICATION_CREDENTIALS
环境变量设置为该文件的路径。
npm
Yarn
pnpm
npm
install
google-auth-library
yarn
add
google-auth-library
pnpm
add
google-auth-library
ChatGoogleVertexAI 类的工作方式与其他基于聊天的 LLM 相同，具有一些例外情况:
第一个传入的
SystemChatMessage
被映射到 PaLM 模型期望的 "context" 参数。
不允许出现其他
SystemChatMessage
。
在第一个
SystemChatMessage
之后，必须是一串奇数条消息，代表人类和模型之间的对话。
发送的信息必须交错出现，先是人类信息，然后是 AI 回复，然后是人类信息，以此类推。
import
{
ChatGoogleVertexAI
}
from
"langchain/chat_models/googlevertexai"
;
const
model
=
new
ChatGoogleVertexAI
(
{
temperature
:
0.7
,
}
)
;
此外，还有一个可选的“例子”构造参数，可以帮助模型理解什么是适当的响应。
看起来像。
import
{
ChatGoogleVertexAI
}
from
"langchain/chat_models/googlevertexai"
;
import
{
AIChatMessage
,
HumanChatMessage
,
SystemChatMessage
,
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
examples
=
[
{
input
:
new
HumanChatMessage
(
"What is your favorite sock color?"
)
,
output
:
new
AIChatMessage
(
"My favorite sock color be arrrr-ange!"
)
,
}
,
]
;
const
model
=
new
ChatGoogleVertexAI
(
{
temperature
:
0.7
,
examples
,
}
)
;
const
questions
=
[
new
SystemChatMessage
(
"You are a funny assistant that answers in pirate language."
)
,
new
HumanChatMessage
(
"What is your favorite food?"
)
,
]
;
// You can also use the model as part of a chain
const
res
=
await
model
.
call
(
questions
)
;
console
.
log
(
{
res
}
)
;
}
;