---
url: https://js.langchain.com.cn/docs/modules/memory/examples/
crawled_at: 2025-06-22T02:00:24.782757
---

示例: 内存
📄️
buffer_memory
缓存内存
📄️
使用缓冲内存与聊天模型翻译的中文结果
本示例介绍如何将聊天特定的内存类与聊天模型配合使用。翻译的中文结果
📄️
Buffer Window Memory
BufferWindowMemory用于跟踪会话中的来回消息，然后使用大小为 k 的窗口将最近的 k 条来回消息提取出来作为内存。
📄️
Conversation Summary（对话总结)
对话总结记忆会在对话进行时对其进行总结并储存在记忆中。这个记忆能够被用于将当前对话总结注入到提示/链中。这个记忆在对较长的对话进行总结时非常有用，因为直接在提示中保留所有过去的对话历史信息将会占用过多的token。
📄️
DynamoDB支持的聊天记录
如果需要在聊天进程之间进行更长期的持久化，您可以将默认的内存chatHistory替换为DynamoDB实例，作为支持BufferMemory等聊天记录类的后端。，注意：chatHistory指聊天记录类，BufferMemory指缓存存储器类。
📄️
实体记忆
实体记忆是会话中记忆特定实体的给定事实。
📄️
Momento支持的聊天记录
如果要在聊天会话中使用分布式、无服务器的持久性,可以使用Momento支持的聊天消息历史记录，即刻缓存，无需任何基础设施维护,无论是在本地构建还是在生产环境中都是一个很好的起点。
📄️
motorhead_memory
Motörhead 是一个由Rust实现的内存服务器。它可以自动处理增量摘要并允许无状态应用程序。
📄️
基于Redis的聊天存储
如果需要在聊天会话之间进行长期持久化，可以将默认的内存chatHistory替换为一个Redis实例来支持聊天存储类，如BufferMemory。
📄️
Upstash 基于 Redis 的聊天记忆
由于 Upstash Redis 通过 REST API 工作,所以您可以将其与 Vercel Edge， [Cloudflare Workers] 一起使用（https：//developers.cloudflare.com/workers/)和其他无服务器环境。
📄️
基于向量库的内存
VectorStoreRetrieverMemory将记忆存储在向量数据库中，并在每次调用时查询最“显著”的前K个文档。
📄️
Zep Memory
Zep是存储、，总结、内嵌、索引和丰富对话AI聊天历史、自治代理历史、文档Q&A历史的记忆服务器，并通过简单、低延迟的API公开它们。