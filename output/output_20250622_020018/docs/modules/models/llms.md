---
url: https://js.langchain.com.cn/docs/modules/models/llms/
crawled_at: 2025-06-22T02:00:25.555119
---

入门指南: LLMs
info
概念指南
LangChain 提供了使用各种 LLM 的标准界面。
要开始， 只需使用
LLM
实现的
call
方法， 传递一个
string
输入。在这个例子中， 我们使用了
OpenAI
实现:
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
model
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
model
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
}
;
深入研究
​
📄️
集成
LangChain提供了多种LLM实现，可与各种模型提供者集成。这些是:
📄️
附加功能
我们为LLM提供了许多附加功能。在下面的大多数示例中，我们将使用 OpenAI LLM。然而，所有这些功能都适用于所有LLMs。