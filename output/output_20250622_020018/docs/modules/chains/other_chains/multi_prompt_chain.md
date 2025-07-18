---
url: https://js.langchain.com.cn/docs/modules/chains/other_chains/multi_prompt_chain
crawled_at: 2025-06-22T02:00:21.403264
---

multi_prompt_chain
MultiPromptChain
多次提示链
​
MultiPromptChain 允许 LLM 从多个提示中进行选择。通过提供一组模板/提示以及它们对应的名称和描述来构建该链。该链接受一个字符串作为输入，选择一个合适的提示，然后将输入传递到所选的提示中。
import
{
MultiPromptChain
}
from
"langchain/chains"
;
import
{
OpenAIChat
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
llm
=
new
OpenAIChat
(
)
;
const
promptNames
=
[
"physics"
,
"math"
,
"history"
]
;
const
promptDescriptions
=
[
"Good for answering questions about physics"
,
"Good for answering math questions"
,
"Good for answering questions about history"
,
]
;
const
physicsTemplate
=
`
You are a very smart physics professor. You are great at answering questions about physics in a concise and easy to understand manner. When you don't know the answer to a question you admit that you don't know.
Here is a question:
{input}
`
;
const
mathTemplate
=
`
You are a very good mathematician. You are great at answering math questions. You are so good because you are able to break down hard problems into their component parts, answer the component parts, and then put them together to answer the broader question.
Here is a question:
{input}
`
;
const
historyTemplate
=
`
You are a very smart history professor. You are great at answering questions about history in a concise and easy to understand manner. When you don't know the answer to a question you admit that you don't know.
Here is a question:
{input}
`
;
const
promptTemplates
=
[
physicsTemplate
,
mathTemplate
,
historyTemplate
]
;
const
multiPromptChain
=
MultiPromptChain
.
fromLLMAndPrompts
(
llm
,
{
promptNames
,
promptDescriptions
,
promptTemplates
,
}
)
;
const
testPromise1
=
multiPromptChain
.
call
(
{
input
:
"What is the speed of light?"
,
}
)
;
const
testPromise2
=
multiPromptChain
.
call
(
{
input
:
"What is the derivative of x^2?"
,
}
)
;
const
testPromise3
=
multiPromptChain
.
call
(
{
input
:
"Who was the first president of the United States?"
,
}
)
;
const
[
{
text
:
result1
}
,
{
text
:
result2
}
,
{
text
:
result3
}
]
=
await
Promise
.
all
(
[
testPromise1
,
testPromise2
,
testPromise3
]
)
;
console
.
log
(
result1
,
result2
,
result3
)
;
}
;