---
url: https://js.langchain.com.cn/docs/modules/chains/other_chains/
crawled_at: 2025-06-22T02:00:21.184037
---

其他链
本节介绍其它存在的链的示例。
📄️
AnalyzeDocumentChain
您可以使用AnalyzeDocumentChain,它接受单个文本作为输入并对其进行操作。
📄️
APIChain
APIChain 可用于使用 LLM 与 API 交互，从而检索相关信息。提供关于所提供的 API 文档相关的问题以构造链。
📄️
宪法链
宪法链是一种链式结构，它确保语言模型的输出遵循预定义的宪法原则。通过纳入特定的规则和指南，宪法链可以过滤和修改生成的内容以符合这些原则，从而提供更加受控、道德和上下文恰当的响应。这种机制有助于保持输出的完整性，同时最大程度地减少生成可能违反指南、具有冒犯性或偏离所需上下文的内容的风险。
📄️
moderation_chain
OpenAIModerationChain
📄️
multi_prompt_chain
MultiPromptChain多次提示链
📄️
multi_retrieval_qa_chain
换行
📄️
SqlDatabaseChain 中文：Sql数据库链
SqlDatabaseChain 可以让您在 SQL 数据库上回答问题。
📄️
摘要
摘要链可以用来总结多个文档。一种方法是在将多个较小的文档分成块后将它们作为输入，与MapReduceDocumentsChain一起操作。您还可以选择将进行摘要的链替换为StuffDocumentsChain，或RefineDocumentsChain。在此处了解有关它们之间差异的更多信息here