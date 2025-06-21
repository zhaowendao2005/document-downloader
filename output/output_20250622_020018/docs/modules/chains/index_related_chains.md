---
url: https://js.langchain.com.cn/docs/modules/chains/index_related_chains/
crawled_at: 2025-06-22T02:00:21.010614
---

与索引相关的链
info
概念指南
与存储在索引中的非结构化数据一起工作相关的链。
📄️
文档QA
LangChain提供了一系列专门针对非结构化文本数据处理的链条: StuffDocumentsChain， MapReduceDocumentsChain， 和 RefineDocumentsChain。这些链条是开发与这些数据交互的更复杂链条的基本构建模块。它们旨在接受文档和问题作为输入，然后利用语言模型根据提供的文档制定答案。
📄️
检索问答
RetrievalQAChain 是将 Retriever 和 QA 链（上文中所述)组合起来的链。它用于从 Retriever 检索文档，然后使用 QA 链根据检索到的文档回答问题。
📄️
对话式检索问答
ConversationalRetrievalQA 链基于 RetrievalQAChain 构建，提供了聊天历史记录组件。