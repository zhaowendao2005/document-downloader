---
url: https://js.langchain.com.cn/docs/modules/indexes/document_loaders/examples/file_loaders/
crawled_at: 2025-06-22T02:00:21.765886
---

文件加载程序
兼容性
仅适用于Node.js。
这些加载程序用于加载给定的文件系统路径或Blob对象的文件。
📄️
具有多个文件夹的文件夹
本示例介绍如何从具有多个文件的文件夹中加载数据。第二个参数是文件扩展名到加载器工厂的映射。每个文件将传递给匹配的加载器， 并将生成的文档连接在一起。
📄️
CSV文件
本示例介绍如何从CSV文件加载数据。
📄️
Docx files
本示例介绍如何从docx文件中加载数据。
📄️
EPUB文件
本例演示如何从EPUB文件中加载数据。默认情况下，每个章节会创建一个文档，您可以通过将“splitChapters”选项设置为“false”来更改此行为。
📄️
JSON文件
JSON加载器使用JSON指针来定位您想要定位的JSON文件中的键。
📄️
JSONLines 文件
这个例子演示了如何从 JSONLines 或 JSONL 文件加载数据。第二个参数是一个 JSONPointer，用于从文件中的每个 JSON 对象中提取属性。每个 JSON 对象都将创建一个文档。
📄️
Notion markdown export
本示例介绍如何从导出的 Notion 页面中加载数据。
📄️
PDF文件
在这个例子中，我们将介绍如何从PDF文件中导入数据。默认情况下，每个页面将创建一个文档。通过将 splitPages 选项设置为 false 可以更改此行为。
📄️
字幕
本示例介绍如何从字幕文件中加载数据。每个字幕文件将创建一个文档。
📄️
文本文件
本例将介绍如何从文本文件中加载数据。
📄️
无结构
本示例介绍如何使用无结构读取多种类型的文件。无结构目前支持加载文本文件、PPT、HTML、PDF、图片等。