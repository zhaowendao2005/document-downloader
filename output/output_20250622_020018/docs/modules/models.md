---
url: https://js.langchain.com.cn/docs/modules/models/
crawled_at: 2025-06-22T02:00:25.235485
---

模型
info
概念指南
模型是LangChain的核心组件。LangChain不是模型的提供者，而是提供标准接口，通过该接口您可以与各种语言模型进行交互。
LangChain支持文本模型(LLMs)，聊天模型和文本嵌入模型。
LLMs使用文本输入和输出，而聊天模型使用消息输入和输出。
注意:
聊天模型API还比较新，因此我们还在找出正确的抽象。如果您有任何反馈，请告诉我们！
所有模型
​
🗃️
聊天模型
2 items
🗃️
嵌入
2 items
🗃️
LLMs
2 items
高级
​
本节面向想要更深入技术了解LangChain工作原理的用户。如果您刚开始使用，请跳过本节。
LLMs和聊天模型都基于
BaseLanguageModel
类构建。该类为所有模型提供了公共接口，并允许我们在不改变其余代码的情况下轻松切换模型。
BaseLanguageModel
类具有两个抽象方法
generatePrompt
和
getNumTokens
，分别由
BaseChatModel
和
BaseLLM
实现。
BaseLLM
是
BaseLanguageModel
的子类，为 LLM（Large Language Model）提供了一个通用的接口，而
BaseChatModel
是
BaseLanguageModel
的子类，为聊天模型提供了一个通用的接口。