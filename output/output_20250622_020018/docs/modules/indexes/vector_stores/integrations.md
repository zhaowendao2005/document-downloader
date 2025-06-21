---
url: https://js.langchain.com.cn/docs/modules/indexes/vector_stores/integrations/
crawled_at: 2025-06-22T02:00:23.680750
---

矢量存储: 集成
📄️
内存
MemoryVectorStore是一个内存中的暂存向量存储器，用于在内存中存储嵌入，并做精确的线性搜索以找到最相似的嵌入。默认的相似度度量是余弦相似度，但可以更改为ml-distance支持的任何相似度度量方式。
📄️
chroma
换行符
📄️
Faiss
仅适用于Node.js环境。
📄️
HNSWLib
仅适用于Node.js。
📄️
Milvus
Milvus是专为嵌入式相似性搜索和 AI 应用而构建的向量数据库。
📄️
MyScale
仅在Node.js上可用。
📄️
OpenSearch
仅限于 Node.js。
📄️
Pinecone
仅适用于 Node.js。
📄️
prisma
---
📄️
Qdrant
Qdrant 是一个向量相似度搜索引擎。它提供了一个方便的API来存储、搜索和管理带有附加有效负载的点 - 向量。
📄️
Redis
Redis是一款快速的开源内存数据存储系统。，作为Redis Stack的一部分，RediSearch是一种支持向量相似性语义搜索以及其他许多类型搜索的模块。
📄️
SingleStore
SingleStoreDB是一款高性能，分布式数据库系统。长期以来，它一直支持dotproduct等向量函数，从而成为需要文本相似度匹配的AI应用程序的最佳解决方案。
📄️
Supabase
Langchain支持使用Supabase Postgres数据库作为向量存储使用'pgvector' postgres扩展。 有关更多信息，请参阅Supabase博客文章。
📄️
仅限node
Tigris使向量嵌入的构建人工智能应用程序变得轻松。
📄️
TypeORM
为了在通用的PostgreSQL数据库中实现向量搜索，LangChainJS支持使用TypeORM和pgvector Postgres扩展。
📄️
Weaviate
Weaviate是一个开源的向量数据库，可以存储对象和向量，使向量搜索与结构化过滤相结合。LangChain通过weaviate-ts-client软件包连接到Weaviate，这是官方的Typescript客户端。