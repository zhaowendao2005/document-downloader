---
url: https://js.langchain.com.cn/docs/modules/prompts/prompt_templates/prompt_composition
crawled_at: 2025-06-22T02:00:25.896527
---

提示组合
流水线提示模板允许您将多个单独的提示模板组合在一起。
当您想重用单个提示的部分时，这可能很有用。
与将
inputVariables
作为参数不同，流水线提示模板需要两个新参数:
pipelinePrompts
: 一个包含字符串 (
name
) 和
PromptTemplate
对象的数组。
每一个
PromptTemplate
会被格式化，然后作为一个输入变量传递给管道中下一个提示模板，并使用与
name
相同的名称。
finalPrompt
: 将返回的最终提示。
以下是实际操作的示例:
import
{
PromptTemplate
,
PipelinePromptTemplate
}
from
"langchain/prompts"
;
const
fullPrompt
=
PromptTemplate
.
fromTemplate
(
`
{introduction}
{example}
{start}
`
)
;
const
introductionPrompt
=
PromptTemplate
.
fromTemplate
(
`
You are impersonating {person}.
`
)
;
const
examplePrompt
=
PromptTemplate
.
fromTemplate
(
`
Here's an example of an interaction:
Q: {example_q}
A: {example_a}
`
)
;
const
startPrompt
=
PromptTemplate
.
fromTemplate
(
`
Now, do this for real!
Q: {input}
A:
`
)
;
const
composedPrompt
=
new
PipelinePromptTemplate
(
{
pipelinePrompts
:
[
{
name
:
"introduction"
,
prompt
:
introductionPrompt
,
}
,
{
name
:
"example"
,
prompt
:
examplePrompt
,
}
,
{
name
:
"start"
,
prompt
:
startPrompt
,
}
,
]
,
finalPrompt
:
fullPrompt
,
}
)
;
const
formattedPrompt
=
await
composedPrompt
.
format
(
{
person
:
"Elon Musk"
,
example_q
:
`
What's your favorite car?
`
,
example_a
:
"Telsa"
,
input
:
`
What's your favorite social media site?
`
,
}
)
;
console
.
log
(
formattedPrompt
)
;
/*
You are impersonating Elon Musk.
Here's an example of an interaction:
Q: What's your favorite car?
A: Telsa
Now, do this for real!
Q: What's your favorite social media site?
A:
*/