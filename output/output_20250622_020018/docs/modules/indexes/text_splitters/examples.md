---
url: https://js.langchain.com.cn/docs/modules/indexes/text_splitters/examples/
crawled_at: 2025-06-22T02:00:23.496525
---

文本分割器: 示例
📄️
字符文本分割器
除了递归字符文本分割器之外，还有更常见的字符文本分割器。
📄️
代码和标记文本分割器
LangChain支持各种不同的标记和编程语言特定的文本分割器，以基于语言特定的语法分割文本。
📄️
RecursiveCharacterTextSplitter
推荐使用的TextSplitter是“递归字符文本分割器”。它会通过不同的符号递归地分割文档-从“”开始，然后是“”，再然后是“ ”。这很好，因为它会尽可能地将所有语义相关的内容保持在同一位置。
📄️
TokenTextSplitter
最后， TokenTextSplitter 将原始文本字符串转换为 BPE 标记，并将这些标记分成块，然后将单个块中的标记转换回文本。#（Finally)