---
url: https://js.langchain.com.cn/docs/modules/schema/example
crawled_at: 2025-06-22T02:00:25.959830
---

示例
示例是输入/输出对，表示对函数的输入和预期输出。它们可用于模型的训练和评估。
type
Example
=
Record
<
string
,
string
>
;
创建示例
​
您可以这样创建示例:
const
example
=
{
input
:
"foo"
,
output
:
"bar"
,
}
;