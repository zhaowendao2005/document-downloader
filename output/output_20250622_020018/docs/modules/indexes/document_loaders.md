---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/
crawled_at: 2025-06-22T02:00:21.700243
---

入门: 文档装载
info
概念指南
文档装载器使得从各种数据源创建
文档
变得容易。这些文档可以被加载到
向量存储器
中以从数据源加载文档。
interface
DocumentLoader
{
load
(
)
:
Promise
<
Document
[
]
>
;
loadAndSplit
(
textSplitter
?
:
TextSplitter
)
:
Promise
<
Document
[
]
>
;
}
文档装载器公开两个方法：
load
和
loadAndSplit
。
load
会从数据源加载文档并将它们作为
文档
数组返回。
loadAndSplit
会从数据源加载文档，使用提供的
文本分割器
对它们进行分割，并将它们作为
文档
数组返回。
所有文档装载器
​
🗃️
示例
2 items
高级
​
如果您想要实现自己的文档装载器，您有几个选择。
子类化
BaseDocumentLoader
​
你可以直接扩展
BaseDocumentLoader
类。
BaseDocumentLoader
类提供了一些方便的方法，可以从各种数据源加载文档。
abstract
class
BaseDocumentLoader
implements
DocumentLoader
{
abstract
load
(
)
:
Promise
<
Document
[
]
>
;
}
子类化
TextLoader
​
如果你想从文本文件中加载文档，你可以扩展
TextLoader
类。
TextLoader
类会负责读取文件，所以你只需实现一个解析方法即可。
abstract
class
TextLoader
extends
BaseDocumentLoader
{
abstract
parse
(
raw
:
string
)
:
Promise
<
string
[
]
>
;
}
子类化
BufferLoader
​
如果你想要从二进制文件中加载文档，你可以扩展
BufferLoader
类。
BufferLoader
类会负责读取文件，因此你只需要实现一个解析方法。
abstract
class
BufferLoader
extends
BaseDocumentLoader
{
abstract
parse
(
raw
:
Buffer
,
metadata
:
Document
[
"metadata"
]
)
:
Promise
<
Document
[
]
>
;
}