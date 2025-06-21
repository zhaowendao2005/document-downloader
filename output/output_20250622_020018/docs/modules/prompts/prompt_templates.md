---
url: https://js.langchain.com.cn/docs/modules/prompts/prompt_templates/
crawled_at: 2025-06-22T02:00:25.767047
---

提示模板
info
概念指南
PromptTemplate
允许您使用模板生成提示。当您想在多个地方使用相同的提示概要，但更改某些值时，这非常有用。
如下所示，
PromptTemplate
对LLM和聊天模型都有支持:
import
{
ChatPromptTemplate
,
HumanMessagePromptTemplate
,
PromptTemplate
,
SystemMessagePromptTemplate
,
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
// A `PromptTemplate` consists of a template string and a list of input variables.
const
template
=
"What is a good name for a company that makes {product}?"
;
const
promptA
=
new
PromptTemplate
(
{
template
,
inputVariables
:
[
"product"
]
}
)
;
// We can use the `format` method to format the template with the given input values.
const
responseA
=
await
promptA
.
format
(
{
product
:
"colorful socks"
}
)
;
console
.
log
(
{
responseA
}
)
;
/*
{
responseA: 'What is a good name for a company that makes colorful socks?'
}
*/
// We can also use the `fromTemplate` method to create a `PromptTemplate` object.
const
promptB
=
PromptTemplate
.
fromTemplate
(
"What is a good name for a company that makes {product}?"
)
;
const
responseB
=
await
promptB
.
format
(
{
product
:
"colorful socks"
}
)
;
console
.
log
(
{
responseB
}
)
;
/*
{
responseB: 'What is a good name for a company that makes colorful socks?'
}
*/
// For chat models, we provide a `ChatPromptTemplate` class that can be used to format chat prompts.
const
chatPrompt
=
ChatPromptTemplate
.
fromPromptMessages
(
[
SystemMessagePromptTemplate
.
fromTemplate
(
"You are a helpful assistant that translates {input_language} to {output_language}."
)
,
HumanMessagePromptTemplate
.
fromTemplate
(
"{text}"
)
,
]
)
;
// The result can be formatted as a string using the `format` method.
const
responseC
=
await
chatPrompt
.
format
(
{
input_language
:
"English"
,
output_language
:
"French"
,
text
:
"I love programming."
,
}
)
;
console
.
log
(
{
responseC
}
)
;
/*
{
responseC: '[{"text":"You are a helpful assistant that translates English to French."},{"text":"I love programming."}]'
}
*/
// The result can also be formatted as a list of `ChatMessage` objects by returning a `PromptValue` object and calling the `toChatMessages` method.
// More on this below.
const
responseD
=
await
chatPrompt
.
formatPromptValue
(
{
input_language
:
"English"
,
output_language
:
"French"
,
text
:
"I love programming."
,
}
)
;
const
messages
=
responseD
.
toChatMessages
(
)
;
console
.
log
(
{
messages
}
)
;
/*
{
messages: [
SystemChatMessage {
text: 'You are a helpful assistant that translates English to French.'
},
HumanChatMessage { text: 'I love programming.' }
]
}
*/
}
;
深入了解
​
📄️
提示组合
流水线提示模板允许您将多个单独的提示模板组合在一起。
📄️
额外功能（Additional Functionality)
我们提供了一些额外的功能，以便在提示模板中展示，如下所示:（We offer a number of extra features for prompt templates as shown below)