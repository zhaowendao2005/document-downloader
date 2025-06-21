---
url: https://js.langchain.com.cn/docs/modules/prompts/example_selectors/
crawled_at: 2025-06-22T02:00:25.716892
---

示例选择器
info
概念指南
如果您有大量的示例,您可能需要以编程方式选择要包含在提示中的示例。 ExampleSelector 是执行此操作的类。 基本接口定义如下。
class
BaseExampleSelector
{
addExample
(
example
:
Example
)
:
Promise
<
void
|
string
>
;
selectExamples
(
input_variables
:
Example
)
:
Promise
<
Example
[
]
>
;
}
它需要公开一个
selectExamples
方法 - 这需要输入变量，然后返回一个示例列表 - 和一个
addExample
方法,用于保存以后选择的示例。每个具体的实现都可以决定如何保存和选择这些示例。 让我们看一些示例。
根据长度选择
​
此
ExampleSelector
根据长度选择要使用的示例。 当您担心构建的提示会超过上下文窗口的长度时，这非常有用。 对于较长的输入,它会选择较少的示例进行包含,而对于较短的输入，则会选择更多示例。
import
{
LengthBasedExampleSelector
,
PromptTemplate
,
FewShotPromptTemplate
,
}
from
"langchain/prompts"
;
export
async
function
run
(
)
{
// Create a prompt template that will be used to format the examples.
const
examplePrompt
=
new
PromptTemplate
(
{
inputVariables
:
[
"input"
,
"output"
]
,
template
:
"Input: {input}\nOutput: {output}"
,
}
)
;
// Create a LengthBasedExampleSelector that will be used to select the examples.
const
exampleSelector
=
await
LengthBasedExampleSelector
.
fromExamples
(
[
{
input
:
"happy"
,
output
:
"sad"
}
,
{
input
:
"tall"
,
output
:
"short"
}
,
{
input
:
"energetic"
,
output
:
"lethargic"
}
,
{
input
:
"sunny"
,
output
:
"gloomy"
}
,
{
input
:
"windy"
,
output
:
"calm"
}
,
]
,
{
examplePrompt
,
maxLength
:
25
,
}
)
;
// Create a FewShotPromptTemplate that will use the example selector.
const
dynamicPrompt
=
new
FewShotPromptTemplate
(
{
// We provide an ExampleSelector instead of examples.
exampleSelector
,
examplePrompt
,
prefix
:
"Give the antonym of every input"
,
suffix
:
"Input: {adjective}\nOutput:"
,
inputVariables
:
[
"adjective"
]
,
}
)
;
// An example with small input, so it selects all examples.
console
.
log
(
await
dynamicPrompt
.
format
(
{
adjective
:
"big"
}
)
)
;
/*
Give the antonym of every input
Input: happy
Output: sad
Input: tall
Output: short
Input: energetic
Output: lethargic
Input: sunny
Output: gloomy
Input: windy
Output: calm
Input: big
Output:
*/
// An example with long input, so it selects only one example.
const
longString
=
"big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else"
;
console
.
log
(
await
dynamicPrompt
.
format
(
{
adjective
:
longString
}
)
)
;
/*
Give the antonym of every input
Input: happy
Output: sad
Input: big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else
Output:
*/
}
根据相似度选择
​
SemanticSimilarityExampleSelector
根据与输入最相似的示例选择示例。 它通过查找具有与输入的余弦相似度最大的嵌入的示例来实现此目的。
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
import
{
SemanticSimilarityExampleSelector
,
PromptTemplate
,
FewShotPromptTemplate
,
}
from
"langchain/prompts"
;
import
{
HNSWLib
}
from
"langchain/vectorstores/hnswlib"
;
export
async
function
run
(
)
{
// Create a prompt template that will be used to format the examples.
const
examplePrompt
=
new
PromptTemplate
(
{
inputVariables
:
[
"input"
,
"output"
]
,
template
:
"Input: {input}\nOutput: {output}"
,
}
)
;
// Create a SemanticSimilarityExampleSelector that will be used to select the examples.
const
exampleSelector
=
await
SemanticSimilarityExampleSelector
.
fromExamples
(
[
{
input
:
"happy"
,
output
:
"sad"
}
,
{
input
:
"tall"
,
output
:
"short"
}
,
{
input
:
"energetic"
,
output
:
"lethargic"
}
,
{
input
:
"sunny"
,
output
:
"gloomy"
}
,
{
input
:
"windy"
,
output
:
"calm"
}
,
]
,
new
OpenAIEmbeddings
(
)
,
HNSWLib
,
{
k
:
1
}
)
;
// Create a FewShotPromptTemplate that will use the example selector.
const
dynamicPrompt
=
new
FewShotPromptTemplate
(
{
// We provide an ExampleSelector instead of examples.
exampleSelector
,
examplePrompt
,
prefix
:
"Give the antonym of every input"
,
suffix
:
"Input: {adjective}\nOutput:"
,
inputVariables
:
[
"adjective"
]
,
}
)
;
// Input is about the weather, so should select eg. the sunny/gloomy example
console
.
log
(
await
dynamicPrompt
.
format
(
{
adjective
:
"rainy"
}
)
)
;
/*
Give the antonym of every input
Input: sunny
Output: gloomy
Input: rainy
Output:
*/
// Input is a measurement, so should select the tall/short example
console
.
log
(
await
dynamicPrompt
.
format
(
{
adjective
:
"large"
}
)
)
;
/*
Give the antonym of every input
Input: tall
Output: short
Input: large
Output:
*/
}