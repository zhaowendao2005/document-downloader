---
url: https://js.langchain.com.cn/docs/modules/models/chat/
crawled_at: 2025-06-22T02:00:25.278714
---

入门: 聊天模型
info
概念指南
LangChain提供了一个标准接口来使用聊天模型。聊天模型是语言模型的一种变体。
虽然聊天模型在内部使用语言模型，但它们公开的接口有些不同。
除了公开一个“输入文本，输出文本”的API外，它们还公开了一个“聊天消息”作为输入和输出的接口。
聊天消息
​
一个“聊天消息”是指聊天模型中的模块化信息单位。
目前，这包括一个“text”字段，它指的是聊天消息的内容。
目前LangChain支持四种不同类型的“聊天消息”:
HumanChatMessage
: 模拟一个人类的视角发送的聊天消息。
AIChatMessage
: 从AI系统的角度发送的聊天消息，用于与人类进行通信。
SystemChatMessage
: 一种用于向AI系统提供有关对话信息的聊天消息。通常在对话开始时发送。
ChatMessage
: 一个通用的聊天消息，不仅有一个“文本”字段，还有一个任意的“角色”字段。
要开始使用，只需使用“LLM”实现的“call”方法，传入一个字符串输入。在这个例子中，我们使用的是“ChatOpenAI”实现:
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
)
;
// Pass in a list of messages to `call` to start a conversation. In this simple example, we only pass in one message.
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
}
;
深入挖掘
​
📄️
集成
LangChain提供了许多与不同模型提供者集成的聊天模型实现。它们如下所示:
📄️
附加功能
我们为聊天模型提供了许多附加功能。在以下示例中，我们将使用 ChatOpenAI 模型。