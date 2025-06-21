---
url: https://js.langchain.com.cn/docs/modules/indexes/retrievers/
crawled_at: 2025-06-22T02:00:22.831287
---

召回器（Retrievers)
info
概念指南
一种存储数据的方式，可以通过语言模型进行查询。这个对象必须公开的唯一接口是一个
getRelevantDocuments
方法，该方法接受一个字符串查询并返回一个文档列表。
📄️
ChatGPT插件检索器
本示例演示如何在LangChain中使用ChatGPT检索器插件。
📄️
自我查询色度检索器
自我查询检索器正如其名称所示具有查询自身的能力。具体而言给定任何自然语言查询检索器使用查询构建LLM链来撰写结构化查询，然后将该结构化查询应用于其基础向量存储中。这使得检索器不仅可以使用用户输入的查询进行与存储文档内容的语义相似性比较，而且可以从用户查询中提取存储文档的元数据过滤器并执行这些过滤器。
📄️
contextual-compression-retriever
上下文压缩检索器
📄️
Databerry Retriever
本示例展示如何在RetrievalQAChain中使用Databerry Retriever从Databerry.ai数据存储库检索文档。
📄️
HyDE Retriever
本示例展示了如何使用HyDE Retriever，其实现了Hypothetical Document Embeddings（HyDE)，具体内容参见这篇论文。
📄️
金属检索器
该示例展示了如何在“检索QAChain”中使用金属检索器从金属索引中检索文档。
📄️
自查Pinecone检索器
自查检索器具备查询自身的能力，正如其名称所示。具体地说，对于任何自然语言查询，检索器使用基于查询结构构建的LLM链来编写结构化查询，然后将该结构化查询应用于其底层向量存储。这不仅允许检索器使用用户输入的查询与所存储文件内容进行语义相似性比较，还可以从用户查询中提取有关存储文档元数据的过滤器并执行这些过滤器。[注：LLM链，指的是“罗杰局部语言模型”，是一种NLP技术]
📄️
远程检索器
本示例展示如何在 RetrievalQAChain 中使用远程检索器从远程服务器检索文档。
📄️
Supabase 混合搜索
Langchain 支持使用 Supabase Postgres 数据库进行混合搜索。该混合搜索结合了 Postgres 的 pgvector 扩展（相似度搜索)和全文搜索（关键词搜索)来检索文档。您可以通过 SupabaseVectorStore 的 addDocuments 函数添加文档。SupabaseHybridKeyWordSearch 接受嵌入， supabase 客户端， 相似性搜索的结果数量， 和关键词搜索的结果数量作为参数。getRelevantDocuments 函数产生一个去重和按相关性分数排序的文档列表。
📄️
时间加权召回器
时间加权召回器是一种综合考虑相似性和新近度的召回器。评分算法为 :。
📄️
向量库
一旦您创建了一个向量库， ,使用它作为检索器就非常简单:
📄️
Vespa Retriever
展示如何使用Vespa.ai作为LangChain检索器。
📄️
Zep Retriever
这个示例展示了如何在 RetrievalQAChain 中使用 Zep Retriever 从 Zep 内存存储中检索文档。(This example shows how to use the Zep Retriever in a RetrievalQAChain to retrieve documents from Zep memory store.)