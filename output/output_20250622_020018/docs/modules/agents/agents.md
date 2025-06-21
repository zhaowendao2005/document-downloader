---
url: https://js.langchain.com.cn/docs/modules/agents/agents/
crawled_at: 2025-06-22T02:00:19.823419
---

代理
info
概念指南
代理是一个无状态的封装器，封装了一个代理提示链（比如MRKL)，负责将工具格式化到提示符中，以及解析从聊天模型获取的响应。它接收用户输入，并返回相应的“操作”和相应的“操作输入”响应。
选择哪种代理？
​
您选择的代理取决于您想执行的任务类型。以下是一个快速指南，可帮助您为您的使用情况选择正确的代理:
如果您正在使用文本LLM， 首先尝试
zero-shot-react-description
， 即。
LLMs的MRKL代理
。
如果您正在使用聊天模型， 尝试
chat-zero-shot-react-description
， 即。
聊天模型的MRKL代理
。
如果您正在使用聊天模型并想使用内存， 尝试
chat-conversational-react-description
，
会话代理
。
如果您有一个需要多个步骤的复杂任务，并且您有兴趣尝试一种新的代理类型， 尝试
Plan-and-Execute代理
。
所有代理
​
🗃️
动作代理 Action Agents
4 items
📄️
计划执行代理
这个例子展示了如何使用一个使用计划执行框架来回答查询的代理。
🗃️
自定义代理
3 items